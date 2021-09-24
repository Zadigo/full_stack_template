from django.utils import http
from rest_framework import status
from api.serializers.authentication import LoginSerializer, SignupSerializer
from api.serializers.profile import MyUserProfileSerializer
from api.views import mixins
from api.views.base import base_bad_request_response, base_error_response
from django.contrib.auth import login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.authentication import get_user_model
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

USER_MODEL = get_user_model()


@api_view(['post'])
def login_user(request, **kwargs):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return serializer.authenticate_user(request)


@api_view(['post'])
def logout_user(request, **kwargs):
    if request.user.is_anonymous:
        return Response(data={'error': 'User not authenticated'}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.auth_token.delete()
    logout(request)
    return Response(data={'message': 'User logged out'})


@api_view(['post'])
def signup(request, **kwargs):
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    if not serializer.test_passwords():
        return base_bad_request_response(request, 'Passwords do not match')

    new_user = serializer.save()
    new_user.is_active = True
    new_user.save()

    return Response(data={'message': 'Please login'})


@api_view(['post'])
def get_user_token(request):
    email = request.data.get('email', None)
    if email is None:
        return base_error_response(request)

    user = get_object_or_404(USER_MODEL.objects.all(), email__iexact=email)
    return Response({'token': user.auth_token.key})


@api_view(['post'])
def reset_password(request):
    email_field_name = USER_MODEL.get_email_field_name()

    if request.user.is_authenticated:
        return base_bad_request_response(request, 'User authenticated')

    def send_mail(user, email, current_site, use_https=False):
        context = {
            'email': email,
            'domain': current_site.domain,
            'site_name': current_site.name,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': 'https' if use_https else 'http',

        }
        subject = loader.render_to_string('subject.txt', context)
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string('body.txt', context)

        email_sender = EmailMultiAlternatives(subject, body, '', [email])
        html_email = loader.render_to_string('body.html', context)
        email_sender.attach(html_email, 'text/html')
        email_sender.send()

    def get_users(email):
        active_users = USER_MODEL.objects.filter(
            **{f'{email_field_name}__iexact': email}
        )
        return active_users

    def single_link_generator(email):
        current_site = get_current_site(request)
        for user in get_users(email):
            send_mail(user, getattr(user, email_field_name), current_site=current_site)

    email = request.data.get('email', None)
    if email is None:
        return base_error_response(request)

    single_link_generator(email)
    return Response({'message': 'Email sent'})


def confirm_password_reset(request, **kwargs):
    pass
