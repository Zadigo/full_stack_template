from django.conf.urls import include, url
from django.urls.conf import path
from rest_framework.routers import DefaultRouter

from api.views import authentication, profile, admin

app_name = 'api'

router = DefaultRouter()
router.register(r'profile', profile.ProfileDetails)
router.register(r'users', admin.UsersViewset, basename='users')
router.register(r'addresses', profile.UserAddresses, basename='addresses')


urlpatterns = [
    # Tests
    url(r'^test', admin.TestEndpoint.as_view(), name='test'),
    url(r'^new-address', profile.AddressesViewset.as_view(), name='new_address'),
    # url(r'^new-address', profile.AddNewAddress.as_view(), name='new_address'),



    url(r'^user-token', authentication.GetUserToken.as_view(), name='token'),

    url(r'^update-details', profile.ChangePersonalDetails.as_view(), name='update_details'),



    url(r'^change-password', profile.ChangePassword.as_view(), name='change_password'),
    url(r'^logout', authentication.Logout.as_view(), name='logout'),
    url(r'^login', authentication.Login.as_view(), name='login'),
    url(r'^signup', authentication.Signup.as_view(), name='signup'),
    
    path('', include((router.urls, app_name))),
]
