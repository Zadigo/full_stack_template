from functools import cached_property
from typing import OrderedDict, Type
from django.apps.registry import apps
from django.contrib.admin.sites import AlreadyRegistered
from django.core.exceptions import ImproperlyConfigured

from django.db.models.base import Model
from django.urls.conf import include, path
from django.contrib.auth import authenticate, login, logout
from rest_framework import fields, status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.serializers import Serializer

DB_TO_REST_FIELDS = {
    'CharField': fields.CharField,
    'IntegerField': fields.IntegerField,
    'UrlField': fields.URLField
}


class DefaultModelsPagination(LimitOffsetPagination):
    default_limit = 100


class ModelAdmin:
    # list_display = []
    exclude = []
    fieldsets = []
    list_per_page = 100
    paginator = DefaultModelsPagination
    search_fields = []
    serializer_class = None

    def __init__(self, model, admin_site):
        self.model = model
        self.options = model._meta
        self.admin_site = admin_site

    @cached_property
    def urls(self):
        return [
            path('', api_view(['get'])(self.index_view)),
            # path('create/', api_view(['post'])(self._create_view)),
            # path('<object_id>/change', api_view(['post', 'patch'])(self._change_view)),
            # path('<object_id>/delete', api_view(['post', 'delete'])(self._delete_view)),
        ]

    def _db_field_to_vue(self, request, db_field):
        pass

    def _get_user_authentication(self, request):
        return {'is_authenticated': request.user.is_authenticated}

    def _view_options(self, request, **kwargs):
        """Return as a preflight the fields that
        can be displayed or changed, the permissions
        and authentication for the for the given 
        current user"""
        return OrderedDict(
            display_fields=self.list_display,
            pagination=self.list_per_page,
            exclude=self.exclude,
            # user=self._get_user_authentication(request)
        )

    def _get_serializer(self, queryset=None, many=False) -> Serializer:
        serializer_fields = {}

        if self.serializer_class is not None:
            serializer = self.serializer_class
        else:
            pass
            # for field, foreign in self.modle._meta.get_fields():
            #     serializer_fields[field.name] = DB_TO_REST_FIELDS[field.name]
            # serializer = type(self.model._meta.model_name, (Serializer), {**serializer_fields})
        
        if queryset is not None:
            return serializer(instance=queryset, many=many)
        
        return serializer

    def index_view(self, request, **kwargs):
        """Main view for the app index"""
        queryset = self.get_queryset(request)
        serializer = self._get_serializer(queryset=queryset, many=True)
        data = {
            **self._view_options(request, **kwargs),
            'data': serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def delete_view(self, request, **kwargs):
        pass

    def create_view(self, request, **kwargs):
        pass

    def change_view(self, request, **kwargs):
        pass

    def get_fields(self, request):
        pass

    def get_ordering(self, request):
        pass

    def get_queryset(self, request):
        queryset = self.model._default_manager.get_queryset()
        ordering = self.get_ordering(request)
        if ordering:
            return queryset.order_by(*ordering)
        return queryset

    def get_paginator(self, request):
        instance = self.paginator()
        return instance.paginate_queryset(self.get_queryset(request), request)

    def get_object(self, request, object_id):
        queryset = self.get_queryset(request)
        model = queryset.model
        field = model._meta.pk
        object_id = field.to_python(object_id)
        try:
            return queryset.get(**{field.name: object_id})
        except (model.DoesNotExist, ValidationError, ValueError):
            return None

    def has_add_permission(self, request):
        pass


class VueAdminSite:
    models = []

    def __init__(self, name='vue-admin'):
        self.registry = OrderedDict()
        self.name = name

    @cached_property
    def urls(self):
        return self.get_urls(), 'vue-admin', self.name

    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff

    def build_app_dict(self, request):
        app_dict = dict()
        for model, model_admin in self.registry.items():
            app_label = model._meta.app_label
            model_dict = {
                'name': model._meta.verbose_name_plural.title(),
                'object_name': model._meta.object_name,
                'perms': {}
            }
            if app_label in app_dict:
                pass
            else:
                app_dict[app_label] = {
                    'name': apps.get_app_config(app_label).verbose_name,
                    'app_label': app_label,
                    'app_url': None,
                    'current_app': self.name,
                    'has_module_perms': None,
                    'models': [model_dict]
                }
        return app_dict

    def get_app_list(self, request):
        return self.build_app_dict(request)

    def get_urls(self):
        urlpatterns = [
            path('', api_view(['get'])(self.index_view)),
            path('login', api_view(['get'])(self.login)),
            path('logout', api_view(['get'])(self.logout))
        ]

        for model, model_admin in self.registry.items():
            pattern = f'{model._meta.app_label}/{model._meta.model_name}/'
            urlpatterns.extend([path(pattern, include(model_admin.urls))])
        return urlpatterns
    
    def register(self, model, model_admin=None):
        model_admin = model_admin or ModelAdmin
        
        if model._meta.abstract:
            raise ImproperlyConfigured('The model is abstract')
        
        if model in self.registry:
            raise AlreadyRegistered('The model is already registered')
        
        if not model._meta.swapped:
            self.registry[model] = model_admin(model, self)

    def index_view(self, request, **kwargs):
        app_list = self.get_app_list(request)
        attrs = {
            'data': {**dict(app_list)},
            'status': status.HTTP_200_OK
        }
        if not self.has_permission(request):
            pass
        return Response(**attrs)

    def login(self, request, **kwargs):
        request.current_app = self.name
        user = authenticate(request, **request.POST)
        login(request, user)
        return Response(data=None, status=status.HTTP_200_OK)

    def logout(self, request, **kwargs):
        logout(request)
        return Response(data={'state': True})

vue_admin = VueAdminSite()
