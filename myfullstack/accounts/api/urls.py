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
        views.delete_account_view,
        name='delete_account'
    ),
    re_path(
        r'^profile/update$',
        views.update_profile_view,
        name='update_profile'
    ),
    re_path(
        r'^profile$',  views.profile_view),
    re_path(
        r'^reset-password/(?P<token>[a-z])$',
        views.confirm_reset_password_view,
        name='reset_password'
    ),
    re_path(
        r'^forgot-password$',
        views.forgot_password_view,
        name='forgot_password'
    ),
    re_path(
        r'^signup$',
        views.signup_view
    )
]
