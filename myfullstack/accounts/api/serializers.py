from accounts.validators import (email_validator, password_validator,
                                 username_validator)
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from promailing import emailing
from promailing.emailing import VerifyAccount
from rest_framework import fields
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.serializers import Serializer

USER_MODEL = get_user_model()


class BaseAuthenticationSerializer(Serializer):
    username = fields.CharField(
        allow_null=True,
        validators=[username_validator]
    )
    email = fields.EmailField()
    password = fields.CharField(validators=[])


class LoginSerializer(Serializer):
    username = fields.CharField(required=False)
    email = fields.EmailField(required=False)
    password = fields.CharField()

    def save(self, **kwargs):
        email = self.validated_data.get('email', None)
        username = self.validated_data.get('username', None)
        if email is None and username is None:
            raise ValidationError(detail=_('No username or email'))

        logic = (
            Q(email=email)
            # TODO: When querying the database,
            # Django returns the first record
            # even when 'username' is None because
            # it considers that useer.username even
            # with None is a valid return object
            # Q(username=username)
        )
        user = get_object_or_404(USER_MODEL, logic)

        if not user.is_active:
            raise ValidationError(detail=_('Account needs verification'))

        result = user.check_password(self.validated_data['password'])
        if not result:
            raise ValidationError(detail=_('User could not be authenticated'))

        instance, state = Token.objects.get_or_create(user=user)
        serialized_profile = ProfileSerializer(instance=user.userprofile)
        return {
            'token': instance.key,
            **serialized_profile.data
        }


class SignupSerializer(Serializer):
    username = fields.CharField(validators=[username_validator])
    email = fields.EmailField(validators=[email_validator])
    firstname = fields.CharField(required=False)
    lastname = fields.CharField(required=False)
    password1 = fields.CharField()
    password2 = fields.CharField()

    def save(self, **kwargs):
        password1 = self.validated_data['password1']
        password2 = self.validated_data['password2']
        if password1 != password2:
            raise ValidationError(detail=_("Passwords do not match"))

        # password_validator(password1)

        params = {
            'email': self.validated_data['email'],
            'firstname': self.validated_data.get('firstname', None),
            'lastname': self.validated_data.get('lastname', None),
            'username': self.validated_data['username'],
            'password': password1
        }
        user = USER_MODEL.objects.create_user(**params)

        # TODO: Send email validation in order to verify that
        # we are dealing with a valid email address
        instance = VerifyAccount(user)
        instance.send_email()


class ForgotPassword(BaseAuthenticationSerializer):
    email = fields.EmailField()

    def save(self, **kwargs):
        user = get_object_or_404(
            USER_MODEL, email=self.validated_data['email'])
        instance = emailing.ResetPassword(user)
        instance.send_email()


class PasswordResetSerializer(Serializer):
    token = fields.CharField(validators=[])


class NewSubscriptionSerializer(Serializer):
    email = fields.EmailField()


class AddressProfileSerializer(Serializer):
    id = fields.IntegerField(read_only=True)
    street_address = fields.CharField()
    zip_code = fields.CharField()
    country = fields.CharField()


class UserSerializer(Serializer):
    get_full_name = fields.CharField(read_only=True)
    username = fields.CharField(required=False)
    firstname = fields.CharField(required=False)
    lastname = fields.CharField(required=False)
    email = fields.EmailField(required=False)
    is_admin = fields.BooleanField(read_only=True)
    is_staff = fields.BooleanField(read_only=True)
    created_on = fields.DateTimeField(read_only=True)


class ProfileSerializer(Serializer):
    id = fields.IntegerField(read_only=True)
    user = UserSerializer(required=False)
    avatar = fields.FileField(required=False)
    addresses = AddressProfileSerializer(many=True, required=False)

    def save(self, request, **kwargs):
        profile = request.user.userprofile
        # with transaction.atomic():
        profile_data = self.validated_data['user']
        for key, incoming_value in profile_data.items():
            setattr(profile, key, incoming_value)
        profile.save()

        # sid = transaction.savepoint()

        # transaction.savepoint_commit(sid)


class UpdatePasswordSerializer(Serializer):
    old_password = fields.CharField()
    password1 = fields.CharField(validators=[])
    password2 = fields.CharField(validators=[])

    def save(self, request, **kwargs):
        user = request.user
        result = user.check_password(self.validated_data['old_password'])
        if not result:
            raise AuthenticationFailed(detail='Could not authenticate user')
        user.set_password(self.validated_data['password1'])
