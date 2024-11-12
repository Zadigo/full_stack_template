import re

from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import (authenticate, get_user_model,
                                 password_validation)
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.utils.translation import gettext_lazy as _

USER_MODEL = get_user_model()


class SignupForm(forms.Form):
    """Signup form"""

    email = forms.EmailField(required=False)
    username = forms.CharField(required=False)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    # def is_business_email(self):
    #     # A validator that checks that the email
    #     # domain is a business one
    #     unauthorized_domains = ['gmail', 'outlook', 'live', 'laposte']
    #     email = self.cleaned_data['email']
    #     _, rhv = email.split('@')

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        # Passwords should match
        if password1 != password2:
            self.add_error(
                'password1',
                _('Passowords do not match')
            )

        # Password should be at least of
        # ten characters
        if len(password1) < 10:
            self.add_error(
                'password1',
                _('Password should be at least 10')
            )

        # Password should have at least one
        # capital letter
        has_one_capital_letter = re.search(r'[A-Z]', password1)
        if not has_one_capital_letter:
            self.add_error(
                'password1',
                _('Password should have at least a capital letter')
            )

        validate_password(password1)
        return self.cleaned_data

    def save(self, request, user):
        instance = ActivateAccountEmail(request)
        instance.popoluate_user_cache_from_object(user)
        instance.send()


class AdditionalInformationForm(forms.Form):
    lastname = forms.CharField()
    firstname = forms.CharField()

    def __init__(self, user=None, **kwargs):
        self.user_cache = user
        super().__init__(**kwargs)

    def clean(self):
        if self.user_cache is not None:
            pass
        return self.cleaned_data


class ResetPasswordForm(forms.Form):
    """Allows a user to ask for a reset
    passoword link"""
    email = forms.EmailField(
        max_length=254,
        required=True
    )

    def save(self, request):
        email = self.cleaned_data['email']
        instance = ForgotPasswordEmail(request)
        instance.populate_user_cache_from_model(email, USER_MODEL)
        if instance.has_errors:
            for error in instance.errors:
                self.add_error(None, error)
        else:
            instance.send()


class ResetPasswordConfirmForm(forms.Form):
    """Allows a user to ask for a reset
    passoword link"""
    password1 = forms.CharField(
        max_length=254,
        required=True,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        max_length=254,
        required=True,
        widget=forms.PasswordInput()
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data.get['password2']

        if password1 and password2:
            if password1 != password2:
                raise exceptions.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch'
                )
        password_validation.validate_password(password2, self.user)
        return password2


class CustomAdminAuthenticationForm(AdminAuthenticationForm):
    """Form to login to the Django admin
    when using a custom created model"""

    def clean(self):
        # Despite using email, the "username"
        # field stays the same aka "username"
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if email is not None and password:
            self.user_cache = authenticate(
                self.request,
                email=email,
                password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class CustomUserCreationForm(UserCreationForm):
    """Custom form used to creating users
    in Django's Admin when using a custom
    user model"""

    class Meta:
        model = USER_MODEL
        fields = ['email']


class CustomUserChangeForm(UserChangeForm):
    """Custom form used to updating users
    in Django's Admin when using a custom
    user model"""

    class Meta:
        model = USER_MODEL
        fields = '__all__'
