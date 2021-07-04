from accounts import get_userprofile_model
from django.contrib.auth import get_user_model
from rest_framework import fields
from rest_framework.serializers import ModelSerializer, Serializer

from accounts.models import Address, Payment

USER_MODEL = get_user_model()

USER_PROFILE_MODEL = get_userprofile_model()


class LoginSerializer(Serializer):
    username = fields.CharField()
    password = fields.CharField()


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['reference', 'card', 'iban']


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['street_address', 'zip_code', 'country']



class UserSerializer(ModelSerializer):    
    class Meta:
        model = USER_MODEL
        fields = ['id', 'username', 'firstname', 'lastname', 'email',
                  'is_admin', 'is_staff', 'is_active','is_superuser']


class MyUserProfileSerializer(ModelSerializer):
    myuser = UserSerializer()

    class Meta:
        model = USER_PROFILE_MODEL
        fields = ['id', 'customer_id', 'myuser']
