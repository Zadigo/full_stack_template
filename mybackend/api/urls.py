from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api.views import authentication, profile

router = DefaultRouter()
router.register('profile', profile.ProfileDetails)
# router.register('signup', authentication.Signup)

app_name = 'api'

urlpatterns = [
    url(r'^user-token', authentication.GetUserToken.as_view(), name='token'),
    url(r'^login', authentication.Login.as_view(), name='login'),
    url(r'^signup', authentication.Signup.as_view(), name='signup'),
    url(r'^', include(router.urls)),
]
