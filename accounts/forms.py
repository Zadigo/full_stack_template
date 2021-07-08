from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import authenticate


class CustomAdminAuthenticationForm(AdminAuthenticationForm):
    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

