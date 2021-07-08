from django.contrib import admin
from django.contrib.admin import AdminSite

from accounts.forms import CustomAdminAuthenticationForm
from accounts.models import Address, MyUser, MyUserProfile, Payment
from rest_framework.authtoken.models import TokenProxy
from rest_framework.authtoken.admin import TokenAdmin


class CustomAdminSite(AdminSite):
    login_form = CustomAdminAuthenticationForm

admin_site = CustomAdminSite(name='MyAdmin')


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'firstname', 'lastname', 'is_active', 'is_superuser', 'is_admin']


class MyUserProfileAdmin(admin.ModelAdmin):
    list_display = ['myuser']


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['reference']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['street_address', 'zip_code']


admin_site.register(MyUser, MyUserAdmin)
admin_site.register(MyUserProfile, MyUserProfileAdmin)
admin_site.register(Payment, PaymentsAdmin)
admin_site.register(Address, AddressAdmin)
admin_site.register(TokenProxy, TokenAdmin)
