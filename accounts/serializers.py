from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import fields
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer

from accounts.validators import password_validator, username_validator

USER_MODEL = get_user_model()


class BaseAuthenticationSerializer(Serializer):
    username = fields.CharField(
        allow_null=True,
        validators=[username_validator]
    )
    email = fields.EmailField()
    password = fields.CharField(validators=[])


class LoginSerializer(BaseAuthenticationSerializer):
    def save(self, request, **kwargs):
        result = request.user.check_password(self.validated_data['password'])
        if not result:
            raise ValidationError(detail='User could not be authenticated')
        return result


class SignupSerializer(BaseAuthenticationSerializer):
    password = None
    firstname = fields.CharField(required=False)
    lastname = fields.CharField(required=False)
    password1 = fields.CharField(validators=[password_validator])
    password2 = fields.CharField(validators=[password_validator])

    def save(self, **kwargs):
        password1 = self.validated_data['password1']
        password2 = self.validated_data['password2']
        if password1 != password2:
            raise ValidationError(detail="Passwords do not match")
        params = {
            'email': self.validated_data['email'],
            'firstname': self.validated_data['firstname'],
            'lastname': self.validated_data['lasttname'],
            'username': self.validated_data['username'],
            'password': password2
        }
        USER_MODEL.objects.create(**params)


class ForgotPassword(BaseAuthenticationSerializer):
    username = None
    password = None


class PasswordResetSerializer(Serializer):
    token = fields.CharField(validators=[])


class NewSubscriptionSerializer(Serializer):
    email = fields.EmailField()


class AddressProfileSerializer(Serializer):
    id = fields.IntegerField(read_only=True)
    street_address = fields.CharField()
    zip_code = fields.CharField()
    country = fields.CharField()


class ProfileSerializer(Serializer):
    id = fields.IntegerField(read_only=True)
    firstname = fields.CharField(required=False)
    lastname = fields.CharField(required=False)
    avatar = fields.FileField(required=False)
    addresses = AddressProfileSerializer(many=True, required=False)
    created_on = fields.DateField(read_only=True)

    def save(self, request, **kwargs):
        profile = request.user.myuserprofile_set.get()
        data = request.data
        addresses = data.pop('addresses')
        for key, value in data.items():
            setattr(profile, key, value)
        profile.save()
        for address in addresses:
            instance = profile.addresses.get(id=address['id'])
            for key, value in address.items():
                setattr(instance, key, value)
            instance.save()
