from api import serializers
from api.views import mixins
from django.contrib.auth import login, logout
from django.views.decorators.http import require_GET, require_POST
from rest_framework import status
from rest_framework.authentication import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
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


class GetUserToken(ObtainAuthToken):
    pass


class GetUserToken(GenericAPIView):
    http_method_names = ['get']

    def get(self, request, **kwargs):
        user = request.user
        if user.is_authenticated:
            user = get_object_or_404(USER_MODEL, username=user.username)
            token = Token.objects.get(user=user)
            return Response({'token': token.key})
        return Response({'token': None})
