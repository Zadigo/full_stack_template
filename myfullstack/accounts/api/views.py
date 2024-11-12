from accounts.api import serializers
from accounts.api.permissions import HasPermissions, IsAuthenticated
from accounts.models import CustomUser, UserProfile
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotAcceptable, PermissionDenied
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     RetrieveUpdateAPIView, UpdateAPIView)
from rest_framework.permissions import AllowAny

USER_MODEL = get_user_model()


class SignupApi(CreateAPIView):
    serializer_class = serializers.SignupSerializer


class ProfileApi(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, **{'user': self.request.user})
        self.check_object_permissions(self.request, obj)
        return obj


class UpdatePasswordApi(UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UpdatePasswordSerializer
    permission_classes = [IsAuthenticated]


class ConfirmResetPassword(UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UpdatePasswordSerializer


@api_view(['post'])
@permission_classes([AllowAny])
def forgot_password_view(request, **kwargs):
    serializer = serializers.ForgotPassword(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return api_response(data={'state': True})


class DestroyAcccountApi(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


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
