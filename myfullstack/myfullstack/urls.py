from accounts.sites import custom_admin_site
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_spectacular import views as drf_views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path(
        '__debug__/',
        include('debug_toolbar.urls')
    ),
    path(
        'auth/v1/token/verify/',
        jwt_views.TokenVerifyView.as_view(),
        name='token_verify'
    ),
    path(
        'auth/v1/token/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'auth/v1/token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api/schema/',
        drf_views.SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        'api/schema/swagger-ui/',
        drf_views.SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/schema/redoc/',
        drf_views.SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
    path(
        'api/rest-framework/',
        include('rest_framework.urls'),
        name='rest_framework'
    ),
    path(
        'api/v1/accounts/',
        include('accounts.api.urls')
    ),
    path(
        'admin/custom',
        custom_admin_site.urls
    ),
    path(
        'admin/',
        admin.site.urls
    )
]
