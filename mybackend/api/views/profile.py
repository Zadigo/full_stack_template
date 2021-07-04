from accounts import get_userprofile_model
from api import serializers
from api.views import mixins
from django.contrib.auth import (authenticate, get_user_model,
                                 update_session_auth_hash)
from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

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


class AddNewAddress(mixins.RestrictedGlobalAPIMixin, GenericAPIView):
    http_method_names = ['post']
    queryset = USER_PROFILE_MODEL.objects.all()
    serializer_class = serializers.AddressSerializer

    def post(self, request, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user.addresses.create(**serializer.data)
        except:
            return Response({'error': 'Address was not created'}, status=status.HTTP_501_NOT_IMPLEMENTED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
