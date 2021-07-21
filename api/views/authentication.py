from api import check_user_token, serializers
from api.views import mixins
from api.views.base import base_error_response
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

USER_MODEL = get_user_model()


class Login(mixins.GlobalAPIMixins, GenericAPIView):
    # http_method_names = ['post']
    serializer_class = serializers.LoginSerializer
    queryset = USER_MODEL.objects.all()

    def perform_authentication(self, request, credentials: dict={}):
        if not credentials:
            return request.user

        email = credentials['email']
        password = credentials['password']
        return authenticate(request, email=email, password=password)

    def perform_login(self, credentials: dict):
        user = self.perform_authentication(self.request, credentials=credentials)
        if not user:
            return False, False, False
        login(self.request, user)
        return Token.objects.get(user=user), serializers.UserSerializer(instance=user), user

    def post(self, request, *args, **kwargs):
        token, serializer, user = self.perform_login(request.data)
        if not serializer:
            return Response({'error': 'The email and/or password were not correct'}, status=status.HTTP_202_ACCEPTED)
        profile_serializer = serializers.MyUserProfileSerializer(instance=user.myuserprofile)
        return Response({'token': token.key, 'details': profile_serializer.data})


class Logout(mixins.GlobalAPIMixins, GenericAPIView):
    def post(self, request, **kwargs):
        logout(request)
        return Response({'state': True})


class Signup(mixins.GlobalAPIMixins, CreateAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = serializers.UserSerializer

    def get_user(self, username: str):
        try:
            return self.queryset.get(username__iexact=username)
        except:
            return False

    def create(self, request, *args, **kwargs):
        credentials = request.data

        if self.get_user(credentials['username']):
            return Response({'error': 'User exists'}, status=status.HTTP_501_NOT_IMPLEMENTED)

        password1 = credentials.pop('password1')
        password2 = credentials.pop('password2')

        if password1 != password2:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_501_NOT_IMPLEMENTED)

        user = USER_MODEL.objects.create_user(**credentials, password=password1)
        _ = Token.objects.create(user=user)
        
        return Response({'state': 'created'}, status=status.HTTP_201_CREATED)


# class GetUserToken(ObtainAuthToken):
#     pass


# class GetUserToken(GenericAPIView):
#     http_method_names = ['get']

#     def get(self, request, **kwargs):
#         user = request.user
#         if user.is_authenticated:
#             user = get_object_or_404(USER_MODEL, username=user.username)
#             token = Token.objects.get(user=user)
#             return Response({'token': token.key})
#         return Response({'token': None})


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
    return Response({})


@api_view(['post'])
def change_password(request):
    if not check_user_token(request):
        return base_error_response(request)

    old_password = request.data.get('old_password')
    password1 = request.data.get('password1')
    password2 = request.data.get('password2')

    if password1 and password2:
        if password1 != password2:
            return base_error_response(request)

    user = get_object_or_404(USER_MODEL.objects.all(), id=request.user.id)
    password_validation.validate_password(old_password, request.user, password_validators=[])

    user.set_password(password1)
    update_session_auth_hash(request, user)
    return Response()
