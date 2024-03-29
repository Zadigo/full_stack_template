from django.conf.urls import include, url
from django.urls.conf import path
from django.views.generic import base
from rest_framework.routers import DefaultRouter

from api.views import admin, authentication, base, profile
from api.vue_admin import vue_admin
# import api._testing

app_name = 'api'

router = DefaultRouter()
router.register(r'users', admin.UsersViewset, basename='users')
router.register(r'addresses', profile.AddressesApi, basename='address')


token_url_patterns = [
    url(r'^$', authentication.get_user_token),
]

authentication_url_patterns = [
    url(r'^login', authentication.login_user),
    url(r'^logout', authentication.logout_user),
    url(r'^signup', authentication.signup),
    url(r'^forgot-password', authentication.forgot_password)
]


profile_url_patterns = [
    url(r'^update/personal-details', profile.update_personal_details),
    url(r'^update/preferences', profile.update_preferences),
    url(r'^(?P<pk>\d+)/password/change', profile.change_password),
    url(r'^$', profile.collect_user_details),
]


urlpatterns = [
    path('tokens/', include(token_url_patterns)),
    path('auth/', include(authentication_url_patterns)),
    path('profile/', include(profile_url_patterns)),

    url(r'^subscribe', base.subscribe_user),
    path('', include((router.urls, app_name))),

    # Tests
    # url(r'^test', admin.TestEndpoint.as_view(), name='test'),

    # Admin
    path('vue/', vue_admin.urls)
]
