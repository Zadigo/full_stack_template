from accounts.tasks import send_account_creation_email
from accounts.validators import email_validator, username_validator
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import fields
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.serializers import Serializer

USER_MODEL = get_user_model()


class SignupSerializer(Serializer):
    username = fields.CharField(validators=[username_validator])
    email = fields.EmailField(validators=[email_validator])
    firstname = fields.CharField(write_only=True, required=False)
    lastname = fields.CharField(write_only=True, required=False)
    password1 = fields.CharField(write_only=True)
    password2 = fields.CharField(write_only=True)

    def validate(self, attrs):
        password1 = attrs['password1']
        password2 = attrs['password2']

        if password1 != password2:
            raise ValidationError(detail=_("Passwords do not match"))
        return attrs

    def create(self, validated_data):
        password1 = validated_data['password1']
        validate_password(password1)

        params = {
            'email': validated_data['email'],
            'firstname': validated_data.get('firstname', None),
            'lastname': validated_data.get('lastname', None),
            'username': validated_data['username'],
            'password': password1
        }

        user = USER_MODEL.objects.create_user(**params)
        send_account_creation_email.s(user.email)
        return user


class ForgotPassword(Serializer):
    email = fields.EmailField()

    def update(self, instance, validated_data):
        user = get_object_or_404(
            USER_MODEL,
            email=validated_data['email']
        )
        return user


class PasswordResetSerializer(Serializer):
    email = fields.EmailField(read_only=True)



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
    user = UserSerializer(read_only=True, required=False)
    avatar = fields.FileField(required=False)
    addresses = AddressProfileSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UpdatePasswordSerializer(Serializer):
    old_password = fields.CharField(read_only=True)
    password1 = fields.CharField(read_only=True)
    password2 = fields.CharField(read_only=True)

    def update(self, instance, validated_data):
        result = instance.check_password(validated_data['old_password'])
        if not result:
            raise AuthenticationFailed(detail='Could not authenticate user')
        instance.set_password(validated_data['password1'])
        return instance
