# TODO: Find a way to get the current
# active admin site
from accounts.admin import admin_site
from django.contrib import admin

from promailing.models import EmailVerificationCode


class EmailVerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['verification_code', 'expired']
    actions = ['flush']

    def flush(self, request, queryset):
        for item in queryset:
            if item.expired:
                item.delete()

admin_site.register(EmailVerificationCode, EmailVerificationCodeAdmin)
