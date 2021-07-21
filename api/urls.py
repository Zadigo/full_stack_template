from django.conf.urls import include, url
from django.urls.conf import path
from django.views.generic import base
from rest_framework.routers import DefaultRouter
from api.views import authentication, profile, admin

app_name = 'api'

router = DefaultRouter()
# router.register(r'profile', profile.refresh_user_details, basename='profile')
router.register(r'users', admin.UsersViewset, basename='users')
router.register(r'addresses', profile.AddressesApi, basename='address')
# router.register(r'addresses', profile.UserAddresses, basename='addresses')
# router.register(r'delete-address', profile.DeleteAddress, basename='delete_address')

urlpatterns = [
    # Tests
    url(r'^test', admin.TestEndpoint.as_view(), name='test'),


    url(r'^tokens/retrieve', authentication.get_user_token),

    url(r'^update-details', profile.change_personal_details),
    url(r'^preferences', profile.update_preferences),

    url(r'^profile', profile.refresh_user_details),

    url(r'^password/reset', authentication.reset_password),
    url(r'^change-password', profile.ChangePassword.as_view()),

    url(r'^logout', authentication.Logout.as_view()),
    url(r'^login', authentication.Login.as_view()),
    url(r'^signup', authentication.Signup.as_view()),
    
    path('', include((router.urls, app_name))),
]
