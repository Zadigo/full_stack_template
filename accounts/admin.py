from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import TokenProxy

from accounts import forms
from accounts.forms import CustomAdminAuthenticationForm
from accounts.models import Address, MyUser, MyUserProfile, Payment

from django.contrib.auth.admin import UserAdmin


class CustomAdminSite(AdminSite):
    login_form = CustomAdminAuthenticationForm

admin_site = CustomAdminSite(name='MyAdmin')


class MyUserAdmin(admin.ModelAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    
    form = forms.MyUserChangeForm
    add_form = forms.MyUserCreationForm

    list_display = ['email', 'firstname', 'lastname', 'is_active', 'is_superuser', 'is_admin']
    fieldsets = [
        (None, {'fields': ['username', 'password']}),
        (_('Personal info'), {'fields': ['firstname', 'lastname', 'email']}),
        (_('Permissions'), {'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']}),
        (_('Important dates'), {'fields': ['last_login']}),
    ]
    
    filter_horizontal = ['groups', 'user_permissions']
    list_filter = ['is_staff', 'is_superuser', 'is_active',  'groups']
    search_fields = ['username', 'firstname', 'lastname', 'email']
    ordering = ['email']


class MyUserProfileAdmin(admin.ModelAdmin):
    list_display = ['myuser']


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['reference', 'card']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['street_address', 'zip_code']


admin_site.register(MyUser, MyUserAdmin)
admin_site.register(MyUserProfile, MyUserProfileAdmin)
admin_site.register(Payment, PaymentsAdmin)
admin_site.register(Address, AddressAdmin)
admin_site.register(TokenProxy, TokenAdmin)
