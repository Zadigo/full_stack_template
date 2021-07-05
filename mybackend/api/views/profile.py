from django import http
from accounts.models import Address
from accounts import get_userprofile_model
from api import serializers
from api.views import mixins
from django.contrib.auth import (authenticate, get_user_model,
                                 update_session_auth_hash)
from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db.transaction import atomic

USER_MODEL = get_user_model()

USER_PROFILE_MODEL = get_userprofile_model()


class ProfileDetails(GenericViewSet, RetrieveModelMixin):
    queryset = USER_PROFILE_MODEL.objects.all()
    serializer_class = serializers.MyUserProfileSerializer


class ChangePassword(mixins.GlobalAPIMixins, GenericAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = serializers.UserSerializer

    def post(self, request, **kwargs):
        old_password = request.data['old_password']
        user = authenticate(
            request,
            username=request.user.username,
            password=old_password
        )
        if user is None:
            return Response({'error': 'User does not exist'})
        
        password1 = request.data['password1']
        password2 = request.data['password2']

        if password1 != password2:
            pass
            
        if password1 == old_password:
            pass

        user.set_password(password1)
        user.save()
        update_session_auth_hash(request, user)
        return Response({'state': True})


class AddNewAddress(GenericAPIView):
    queryset = USER_PROFILE_MODEL.objects.all()
    serializer_class = serializers.AddressSerializer

    def post(self, request, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            address = user.myuserprofile.addresses.create(**serializer.data)
        except:
            return Response({'error': 'Address was not created'}, status=status.HTTP_501_NOT_IMPLEMENTED)
        serializer = self.get_serializer(instance=address)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserAddresses(GenericViewSet, ListModelMixin):
    queryset = Address.objects.all()
    serializer_class = serializers.AddressSerializer




class AddressesViewset(GenericAPIView):
    http_method_names = ['post', 'patch', 'options']
    queryset = Address.objects.all()
    serializer_class = serializers.AddressValidationSerializer

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(
            user=request.user, 
            validated_data=serializer.validated_data
        )
        return Response(serializer.data)


    # def update(self, request, **kwargs):
    #     pass

    def patch(self, request, **kwargs):
        user = request.user
        candidates = user.myuserprofile.addresses.filter(
            id=request.data['id']
        )
        try:
            address = candidates.get()
        except:
            return Response({'error': 'Change was not made'})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_address = serializer.update(
            instance=address, 
            validated_data=serializer.validated_data
        )
        serialized_address = self.get_serializer(instance=new_address)
        return Response(serialized_address.data)




class ChangePersonalDetails(GenericAPIView):
    # Dynamically update the data depending 
    # on the incoming position that was
    # included in the incoming POST data
    serializer_classes = [
        serializers.UserValidationSerializer
    ]

    def post(self, request, **kwargs):
        serializer_position = request.data.get('position', None)
        if serializer_position is not None:
            serializer_position = int(serializer_position)
        else:
            return Response({'error': 'An error occured - PF1'})
        serializer = self._get_serializer(
            serializer_position, 
            request.data['content']
        )
        serializer.update(request.user, serializer._validated_data)
        return Response(serializer.data)

    def _get_serializer(self, position, data):
        serializer = self.serializer_classes[position]
        instance = serializer(data=data)
        instance.is_valid(raise_exception=True)
        return instance
