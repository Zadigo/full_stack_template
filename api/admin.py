from accounts.models import MyUser
from django.contrib import admin
from rest_framework import fields
from rest_framework.serializers import Serializer

from api.vue_admin import ModelAdmin, vue_admin

# Register your models here.

class UserSerializer(Serializer):
    email = fields.EmailField()
    firstname = fields.CharField()
    username = fields.CharField()

    def save(self, **kwargs):
        pass

class UserAdmin(ModelAdmin):
    # list_display = ['username', 'email']
    serializer_class = UserSerializer
    fieldsets = [
        (None, {'fields': ['username', 'email']})
    ]


vue_admin.register(MyUser, model_admin=UserAdmin)
