from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from promailing.emailing import VerifyAccount
from promailing import verify_user_code
from promailing.models import EmailVerificationCode
from rest_framework.exceptions import NotAcceptable, PermissionDenied
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from accounts import serializers
from accounts.permissions import HasPermissions, IsAuthenticated


def simple_api_response(serializer):
    from rest_framework.response import Response
    return Response(serializer.data)


def api_response(serializer=None, data=None):
    from rest_framework.response import Response
    if serializer is not None and data is not None:
        return simple_api_response(serializer)

    if serializer is not None:
        return simple_api_response(serializer)

    return Response(data=data)


USER_MODEL = get_user_model()


@api_view(['post'])
@permission_classes([AllowAny])
def signup_view(request, **kwargs):
    serializer = serializers.SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return api_response(data={'state': True})


@api_view(['post'])
@permission_classes([AllowAny])
def login_view(request, **kwargs):
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.save()
    return api_response(data=data)


@api_view(['post'])
@permission_classes([IsAuthenticated])
def logout_view(request, **kwargs):
    token = get_object_or_404(Token, user=request.user)
    token.delete()
    return api_response(data={'state': True})


@api_view(['post'])
@permission_classes([AllowAny])
def forgot_password_view(request, **kwargs):
    serializer = serializers.ForgotPassword(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return api_response(data={'state': True})


@api_view(['post'])
@permission_classes([AllowAny])
def confirm_reset_password_view(request, **kwargs):
    serializer = serializers.PasswordResetSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)


@api_view(['get'])
@permission_classes([IsAuthenticated])
def profile_view(request, **kwargs):
    serializer = serializers.ProfileSerializer(
        instance=request.user.myuserprofile)
    return simple_api_response(serializer)


@api_view(['post'])
@permission_classes([IsAuthenticated, HasPermissions])
def update_profile_view(request, **kwargs):
    """A simple route that points to the correct
    serializers for updating a user's profile"""
    methods = ['details', 'password', 'delete']
    method = request.data.get('method', None)
    if method is None:
        raise PermissionDenied(detail='Cannot execute request')

    if method not in methods:
        raise PermissionDenied(detail='Invalid request')

    if method == 'details':
        serializer = serializers.ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(request)
        return simple_api_response(serializer)
    elif method == 'password':
        serializer = serializers.UpdatePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(request)
        return simple_api_response(serializer)
    elif method == 'delete':
        pass


@api_view(['post'])
@permission_classes([IsAuthenticated, HasPermissions])
def delete_account_view(request, **kwargs):
    user = get_object_or_404(USER_MODEL, user=request.user)
    user.delete()


@api_view(['post'])
@permission_classes([AllowAny])
def request_verification_code_view(request, **kwargs):
    user = get_object_or_404(USER_MODEL, email=request.data['email'])
    if user.is_active:
        raise NotAcceptable(detail='Could not perform request')
    instance = VerifyAccount(user)
    instance.send_email()
    return api_response(data={'state': True})


@api_view(['post'])
@permission_classes([AllowAny])
def verify_account_view(request, **kwargs):
    verification_code = request.data.get('verification_code', None)
    instance = verify_user_code(verification_code=verification_code)
    instance.user.is_active = True
    instance.user.save()
    previous_codes = EmailVerificationCode.objects.filter(user=instance.user)
    previous_codes.delete()
    return api_response(data={'state': True})
