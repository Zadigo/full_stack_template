# from django.contrib import admin
from accounts.admin import admin_site
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin_site.urls),
]
