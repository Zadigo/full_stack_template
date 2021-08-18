from api import check_user_token, serializers
from api.views import mixins
from api.views.base import base_bad_request_response, base_error_response
from django.contrib.auth import (login, logout, password_validation,
                                 update_session_auth_hash)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.authentication import authenticate, get_user_model
from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     get_object_or_404)
from rest_framework.response import Response
from rest_framework.serializers import Serializer

USER_MODEL = get_user_model()


class Login(mixins.GlobalAPIMixins, GenericAPIView):
    http_method_names = ['post']
    serializer_class = serializers.LoginSerializer
    queryset = USER_MODEL.objects.all()

    def _perform_authentication(self, request, serializer: Serializer):
        if not serializer:
            return request.user
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        return authenticate(request, email=email, password=password)

    def _perform_login(self, credentials: dict):
        serialized_credentials = self.get_serializer(data=credentials)
        if not serialized_credentials.is_valid():
            return False, False, False

        user = self._perform_authentication(self.request, serializer=serialized_credentials)
        if not user:
            return False, False, False
        login(self.request, user)
        return Token.objects.get_or_create(user=user), serializers.UserSerializer(instance=user), user

    def post(self, request, *args, **kwargs):
        result, serializer, user = self._perform_login(request.data)
        if not result or not serializer:
            return Response({'error': 'The email and/or password were not correct'}, status=status.HTTP_404_NOT_FOUND)
        token, _ = result
        profile_serializer = serializers.MyUserProfileSerializer(instance=user.myuserprofile)
        # TODO: For whatever reasons, this creates an error
        # when trying to retrieve the person's profile
        return Response({'token': token.key, 'details': profile_serializer.data})


class Logout(mixins.GlobalAPIMixins, GenericAPIView):
    def post(self, request, **kwargs):
        if not request.user.is_anonymous:
            return Response({'message': 'User not authenticated'})
            
        request.user.auth_token.delete()
        logout(request)
        return Response({'message': 'User logged out'})


@api_view(['post'])
def signup(request, **kwargs):
    refixed_credentials = {
        'email': request.data.get('email'),
        'password': request.data.get('password1'),
        'firstname': request.data.get('firstname'),
        'lastname': request.data.get('lastname'),
        'username': request.data.get('username', None)
    }
    serialized_credentials = serializers.SignupSerializer(data=refixed_credentials)
    serialized_credentials.is_valid(raise_exception=True)

    password1 = request.data.get('password1')
    password2 = request.data.get('password2')

    if password1 != password2:
        return base_bad_request_response(request, 'Passwords do not match')

    new_user = serialized_credentials.save()
    new_user.is_active = True
    new_user.save()

    serialized_user_profile = serializers.MyUserProfileSerializer(instance=new_user.myuserprofile)
    return Response(data=serialized_user_profile.data)


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
