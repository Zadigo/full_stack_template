from api import serializers
from django.contrib.auth import get_user_model
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin)
from rest_framework.viewsets import GenericViewSet

USER_MODEL = get_user_model()

class ProfileDetails(GenericViewSet, RetrieveModelMixin):
    queryset = USER_MODEL.objects.all()
    serializer_class = serializers.UserSerializer
