from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms.fields import EmailField

from accounts.models import MyUser


class CustomAdminAuthenticationForm(AdminAuthenticationForm):
    """Form to login to the Django Admin"""
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


class UsernameField(EmailField):
    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            'autocapitalize': 'none',
            'autocomplete': 'email'
        }


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser
        fields = '__all__'
        field_classes = {'email': UsernameField}


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ['email']
        field_classes = {'email': UsernameField}
