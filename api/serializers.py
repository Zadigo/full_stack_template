from typing import Tuple, Union

from accounts import get_userprofile_model
from accounts.models import Address, Payment
from django.contrib.auth import get_user_model, update_session_auth_hash
from rest_framework import fields
from rest_framework.serializers import ModelSerializer, Serializer

from api.validators import password_validator

USER_MODEL = get_user_model()

USER_PROFILE_MODEL = get_userprofile_model()


class LoginSerializer(Serializer):
    email = fields.EmailField()
    password = fields.CharField()

    # def save(self, firstname=None, lastname=None):
    #     new_user = USER_MODEL.objects.create(**self.validated_data)
    #     new_user.myuserprofile_set.lastname = lastname
    #     new_user.myuserprofile_set.firstname = firstname
    #     new_user.myuserprofile_set.save()
    #     return new_user


class SignupSerializer(ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ['username', 'firstname', 'lastname', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        new_user = USER_MODEL.objects.create_user(
            username=validated_data.get('username'),
            firstname=validated_data.get('firstname'),
            lastname=validated_data.get('lastname'),
            email=validated_data['email'],
            password=validated_data['password'],
        )
        new_user.is_active = True
        new_user.save()
        return new_user


class UserSerializer(ModelSerializer):    
    class Meta:
        model = USER_MODEL
        fields = ['id', 'username', 'firstname', 'lastname', 'email',
                  'is_admin', 'is_staff', 'is_active','is_superuser']


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street_address', 'zip_code', 'country']


class MyUserProfileSerializer(ModelSerializer):
    myuser = UserSerializer()
    addresses = AddressSerializer(many=True)

    class Meta:
        model = USER_PROFILE_MODEL
        fields = ['id', 'customer_id', 'myuser', 'addresses']













class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['reference', 'card', 'iban']





# Serializers created in order to specifically
# update or create incoming data on their
# respective models

class SerializerMixin:
    def _instance_iterator(self, instance, data):
        for key, value in data.items():
            setattr(instance, key, value)
        return instance

    def _check_has_instance(self, instance):
        instance = self.instance or instance
        if instance is None:
            raise ValueError(("A model instance was not passed on the serializer. "
            "Provide one through the update or create method or call "
            "the serializer with a model instance "
            "e.g. Serializer(instance=instance)"))
        return instance

    def update(self, instance=None, validated_data=None):
        # TODO: For whatever reason, myuser is present
        # in the validated data. In which case, check
        # for that and in order to get the true data
        if 'myuser' in validated_data:
            validated_data = validated_data['myuser']
            
        instance = self._check_has_instance(instance)
        updated_instance = self._instance_iterator(instance, validated_data)
        return updated_instance


class PersonalDetailsValidationSerializer(SerializerMixin, Serializer):
    firstname = fields.CharField(source='myuser.firstname', max_length=50, required=False)
    lastname = fields.CharField(source='myuser.lastname', max_length=50, required=False)
    email = fields.EmailField(source='myuser.email', required=False)
    
    def update(self, instance=None, validated_data=None):
        updated_instance = super().update(instance, validated_data)
        return updated_instance.save()


class AddressValidationSerializer(SerializerMixin, Serializer):
    id = fields.ReadOnlyField()
    street_address = fields.CharField(max_length=50)
    # city = fields.CharField(max_length=50)
    zip_code = fields.CharField(max_length=10)
    country = fields.CharField(max_length=50, default='France')

    def create(self, user, validated_data):
        new_address = Address.objects.create(**validated_data)
        user.myuserprofile.addresses.add(new_address)
        return new_address

    def update(self, instance=None, validated_data=None):
        updated_instance = super().update(instance, validated_data)
        updated_instance.save()
        return updated_instance


class PasswordChangeValidationSerializer(SerializerMixin, Serializer):
    old_password = fields.CharField()
    password1 = fields.CharField(validators=[password_validator])
    password2 = fields.CharField(validators=[password_validator])

    def update(self, request, instance=None, validated_data=None) -> Union[Tuple[bool, str]]:
        if validated_data is None:
            validated_data = self._validated_data

        old_password = validated_data['old_password']
        password1 = validated_data['password1']
        password2 = validated_data['password2']

        if password1 != password2:
            return False, 'Passwords do not match'

        # if len(password1) < 5:
        #     return False, 'Password have 5 characters or more'
        
        if old_password == password1:
            return False, 'New password and old password are similar'

        instance.set_password(password1)
        instance.save()
        update_session_auth_hash(request, instance)
        return True, instance
