from django.conf.urls import include, url
from django.urls.conf import path
from rest_framework.routers import DefaultRouter

from api.views import authentication, profile, admin

app_name = 'api'

router = DefaultRouter()
router.register(r'profile', profile.ProfileDetails)
router.register(r'users', admin.UsersViewset, basename='users')


urlpatterns = [
    url(r'^user-token', authentication.GetUserToken.as_view(), name='token'),

    url(r'^new-address', profile.AddNewAddress.as_view(), name='new_address'),
    url(r'^change-password', profile.ChangePassword.as_view(), name='change_password'),
    url(r'^logout', authentication.Logout.as_view(), name='logout'),
    url(r'^login', authentication.Login.as_view(), name='login'),
    url(r'^signup', authentication.Signup.as_view(), name='signup'),
    
    path('', include((router.urls, app_name))),
]
