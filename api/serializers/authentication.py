from api.serializers.profile import MyUserProfileSerializer
from django.contrib.auth import authenticate, get_user_model, login, logout
from rest_framework import fields, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, Serializer

USER_MODEL = get_user_model()

class LoginSerializer(Serializer):
    email = fields.EmailField(validators=[])
    password = fields.CharField(validators=[])

    def authenticate_user(self, request):
        email = self.validated_data['email']
        password = self.validated_data['password']

        user = authenticate(request, email=email, password=password)
        if not user:
            return Response(data={'error': 'Could not authenticate user'}, status=status.HTTP_200_OK)
        login(request, user)

        instance, _ = Token.objects.get_or_create(user=user)
        serializer = MyUserProfileSerializer(instance=user.myuserprofile)
        data = {'token': instance.key, 'details': serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)

    # def save(self, firstname=None, lastname=None):
    #     new_user = USER_MODEL.objects.create(**self.validated_data)
    #     new_user.myuserprofile_set.lastname = lastname
    #     new_user.myuserprofile_set.firstname = firstname
    #     new_user.myuserprofile_set.save()
    #     return new_user

class SignupSerializer(Serializer):
    email = fields.EmailField()
    username = fields.CharField()
    firstname = fields.CharField()
    lastname = fields.CharField()
    password1 = fields.CharField()
    password2 = fields.CharField()

    def test_passwords(self):
        password1 = self.validated_data['password1']
        password2 = self.validated_data['password2']
        return password1 == password2

    def create(self, request):
        validated_data = self.validated_data.copy()

        password = validated_data['password1']
        validated_data.pop('password1')
        validated_data.pop('password2')
        
        new_user = USER_MODEL.objects.create_user(**validated_data, password=password)
        new_user.is_active = True
        return new_user


# class SignupSerializer(ModelSerializer):
#     class Meta:
#         model = USER_MODEL
#         fields = ['username', 'firstname', 'lastname', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         new_user = USER_MODEL.objects.create_user(
#             username=validated_data.get('username'),
#             firstname=validated_data.get('firstname'),
#             lastname=validated_data.get('lastname'),
#             email=validated_data['email'],
#             password=validated_data['password'],
#         )
#         new_user.is_active = True
#         new_user.save()
#         return new_user
