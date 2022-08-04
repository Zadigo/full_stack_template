# from django.contrib import admin
from accounts.admin import admin_site
from django.urls import path
from django.urls.conf import include, re_path

from full_stack_template.views import index, redirect_view

urlpatterns = [
    path('api/v1/accounts/', include('accounts.urls')),
    # path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin_site.urls),
    # re_path(r'^(?:\w+\/)+$', redirect_view),
    path('', index, name='index'),
]
