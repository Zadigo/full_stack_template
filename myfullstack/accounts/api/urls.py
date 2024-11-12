from accounts.api import views
from django.urls.conf import re_path

app_name = 'api_accounts'

urlpatterns = [
    re_path(
        r'^request-verification-code$',
        views.request_verification_code_view,
        name='verification_code'
    ),
    re_path(
        r'^verify-account$',
        views.verify_account_view,
        name='verify_account'
    ),
    re_path(
        r'^profile/delete$',
        views.DestroyAcccountApi.as_view(),
        name='delete_account'
    ),
    re_path(
        r'^profile$',
        views.ProfileApi.as_view(),
        name='profile'
    ),
    re_path(
        r'^change-password$',
        views.UpdatePasswordApi.as_view(),
        name='change_password'
    ),
    re_path(
        r'^reset-password/(?P<token>[a-z])$',
        views.ConfirmResetPassword.as_view(),
        name='confirm_reset_password'
    ),
    re_path(
        r'^forgot-password$',
        views.forgot_password_view,
        name='forgot_password'
    ),
    re_path(
        r'^signup$',
        views.SignupApi.as_view(),
        name='signup'
    )
]
