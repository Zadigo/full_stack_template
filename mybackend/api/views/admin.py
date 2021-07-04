from typing import List
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from django.contrib.auth import get_user_model

from api import serializers

USER_MODEL = get_user_model()

class UsersViewset(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    authentication_classes = []
    queryset = USER_MODEL.objects.all()
    serializer_class = serializers.UserSerializer
