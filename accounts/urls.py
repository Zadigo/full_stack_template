from django.urls.conf import re_path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^request-verification-code$',
            views.request_verification_code_view),
    re_path(r'^verify-account$', views.verify_account_view),
    re_path(r'^profile/delete$', views.delete_account_view),
    re_path(r'^profile/update$', views.update_profile_view),
    re_path(r'^profile$',  views.profile_view),
    re_path(r'^reset-password/(?P<token>[a-z])$',
            views.confirm_reset_password_view),
    re_path(r'^forgot-password$',  views.forgot_password_view),
    re_path(r'^logout$',  views.logout_view),
    re_path(r'^signup$',  views.signup_view),
    re_path(r'^login$',  views.login_view)
]
