from django.contrib.auth import get_user_model
from rest_framework import fields
from rest_framework.serializers import ModelSerializer, Serializer

USER_MODEL = get_user_model()


class LoginSerializer(Serializer):
    username = fields.CharField()
    password = fields.CharField()


class UserSerializer(ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff']
