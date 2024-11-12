from django_analytics.models import AnalyticsVersion

# TODO: Try to find a way to generate a helper function
# to return the custom admin that was created to replace
# the default admin site
from accounts.sites import custom_admin_site
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class AnalyticConfigurationResource(resources.ModelResource):
    class Meta:
        model = AnalyticsVersion
        fields = ['google_analytics', 'google_ads',
                  'google_tag_manager', 'hotjar']


class AnalyticConfigurationAdmin(ImportExportModelAdmin):
    resource_classes = [AnalyticConfigurationResource]
    list_display = ['full_name', 'created_on']
    readonly_fields = ['version']
    date_hierarchy = 'created_on'
    fieldsets = [
        [
            None,
            {'fields': ['version']
             }
        ],
        [
            'Google',
            {
                'fields': [
                    'google_analytics',
                    'google_tag_manager',
                    'google_ads'
                ]
            }
        ],
        [
            'Hotjar',
            {
                'fields': ['hotjar']
            }
        ],
        [
            'Microsoft',
            {
                'fields': ['clarity']
            }
        ],
        [
            'Facebook',
            {
                'fields': ['facebook_pixel']
            }
        ]
    ]
    actions = ['duplicate_container']

    def duplicate_container(self, request, queryset):
        pass


custom_admin_site.register(AnalyticsVersion, AnalyticConfigurationAdmin)
