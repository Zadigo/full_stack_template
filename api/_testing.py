from api.vue_admin import vue_admin
from rest_framework import fields
from rest_framework.serializers import Serializer

from careers.models import Job


class SomeSerializer(Serializer):
    title = fields.CharField()
    subtitle = fields.CharField()


class TestAdmin(vue_admin.ModelAdmin):
    list_display = ['title', 'subtitle']
    serializer_class = SomeSerializer

vue_admin.register(Job, model_admin=TestAdmin)
