from accounts import forms
from accounts.models import CustomUser, UserProfile
from accounts.sites import custom_admin_site
from django.contrib import admin, messages
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.messages import add_message
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser


class CustomUserAdmin(ImportExportModelAdmin):
    form = forms.CustomUserChangeForm
    add_form = forms.CustomUserCreationForm
    add_form_template = 'admin/auth/user/add_form.html'
    change_password_form = AdminPasswordChangeForm
    resource_classes = [CustomUserResource]
    ordering = ['email']
    list_display = [
        'email', 'firstname', 'lastname', 'created_on',
        'is_staff', 'is_superuser', 'is_active'
    ]
    fieldsets = (
        (
            None,
            {
                "fields": ("username", "password")
            }
        ),
        (
            _("Personal info"),
            {
                "fields": ("firstname", "lastname", "email")
            }
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": ("last_login", "created_on")
            }
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ('wide',),
                "fields": ('email', 'password1', 'password2'),
            },
        ),
    )
    date_hierarchy = 'created_on'
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    filter_horizontal = ['user_permissions', 'groups']
    search_fields = ['email', 'firstname', 'lastname']
    actions = [
        'activate', 'deactivate',
        'email_account_activation_link',
        'email_reset_password_link'
    ]

    def activate(self, request, queryset):
        queryset.update(is_active=True)
        message = f'Activated {len(queryset)} accounts'
        add_message(request, messages.SUCCESS, message)

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
        message = f'Deactivated {len(queryset)} accounts'
        add_message(request, messages.SUCCESS, message)

    def email_account_activation_link(self, request, queryset):
        pass

    def email_reset_password_link(self, request, quersyet):
        pass

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        """Use special form for user creation"""
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
    search_fields = ['user__email', 'user__firstname', 'user__lastname']
    date_hierarchy = 'created_on'


custom_admin_site.register(CustomUser, CustomUserAdmin)
custom_admin_site.register(UserProfile, UserProfileAdmin)
