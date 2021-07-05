from accounts import get_userprofile_model
from django.contrib.auth import get_user_model, update_session_auth_hash
from rest_framework import fields
from rest_framework.serializers import ModelSerializer, Serializer
from django.db.transaction import atomic
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
        fields = ['id', 'street_address', 'zip_code', 'country']


class UserSerializer(ModelSerializer):    
    class Meta:
        model = USER_MODEL
        fields = ['id', 'username', 'firstname', 'lastname', 'email',
                  'is_admin', 'is_staff', 'is_active','is_superuser']


class MyUserProfileSerializer(ModelSerializer):
    myuser = UserSerializer()
    addresses = AddressSerializer(many=True)

    class Meta:
        model = USER_PROFILE_MODEL
        fields = ['id', 'customer_id', 'myuser', 'addresses']


# Serializers created in order to specifically
# update or create incoming data on their
# respective models

class SerializerMixin:
    def instance_iterator(self, instance, data):
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
        instance = self._check_has_instance(instance)
        updated_instance = self.instance_iterator(instance, validated_data)
        return updated_instance


class UserValidationSerializer(SerializerMixin, Serializer):
    firstname = fields.CharField(source='myuser.firstname', max_length=50, required=False)
    lastname = fields.CharField(source='myuser.lastname', max_length=50, required=False)
    email = fields.EmailField(source='myuser.email', required=False)
    
    def update(self, instance=None, validated_data=None):
        # for key, value in validated_data.items():
        #     setattr(instance, key, value)
        # instance.save()
        # return instance
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


class PasswordValidationSerializer(Serializer):
    old_password = fields.CharField()
    password1 = fields.CharField()
    password2 = fields.CharField()

    def update(self, request, instance=None, validated_data=None):
        if validated_data is None:
            validated_data = self._validated_data
        old_password = validated_data['old_password']
        password1 = validated_data['password1']
        password2 = validated_data['password2']

        if password1 != password2:
            pass

        if len(password1) < 5:
            pass
        
        if old_password == password1:
            pass

        instance.set_password(password1)
        instance.save()
        update_session_auth_hash(request, instance)
        return instance
