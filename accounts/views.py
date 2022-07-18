from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from accounts import serializers
from accounts.permissions import HasPermissions, IsAuthenticated

USER_MODEL = get_user_model()


@api_view(['post'])
@permission_classes([AllowAny])
def signup_view(request, **kwargs):
    serializer = serializers.SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()


@api_view(['post'])
@permission_classes([AllowAny])
def login_view(request, **kwargs):
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(request)


@api_view(['post'])
@permission_classes([AllowAny])
def logout_view(request, **kwargs):
    if request.user.is_authenticated:
        token = get_object_or_404(Token, user=request.user)
        token.delete()
    return


@api_view(['post'])
@permission_classes([AllowAny])
def forgot_password_view(request, **kwargs):
    serializer = serializers.ForgotPassword(data=request.data)
    serializer.is_valid(raise_exception=True)


@api_view(['post'])
@permission_classes([AllowAny])
def confirm_reset_password_view(request, **kwargs):
    serializer = serializers.PasswordResetSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)


@api_view(['get'])
@permission_classes([IsAuthenticated])
def profile_view(request, **kwargs):
    profile = request.user.myuserprofile_set.get()
    serializer = serializers.ProfileSerializer(instance=profile)


@api_view(['post'])
@permission_classes([IsAuthenticated, HasPermissions])
def update_profile_view(request, **kwargs):
    serializer = serializers.ProfileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)


@api_view(['post'])
@permission_classes([IsAuthenticated, HasPermissions])
def delete_account_view(request, **kwargs):
    user = get_object_or_404(USER_MODEL, user=request.user)
    user.delete()
