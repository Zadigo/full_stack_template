from api.views import mixins
from api import serializers
from accounts import get_userprofile_model
from django.contrib.auth import (authenticate, get_user_model,
                                 update_session_auth_hash)
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
