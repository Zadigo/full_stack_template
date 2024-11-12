from django.contrib import admin
from django_seo.models import LegalBusiness, SEOVersion
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class SEOConfigurationResource(resources.ModelResource):
    class Meta:
        model = SEOVersion


class LegalBusinessResource(resources.ModelResource):
    class Meta:
        model = LegalBusiness
        fields = [
            'legal_name', 'registration_place', 'company_type',
            'siren', 'siret', 'ape', 'founding_date', 'general_email',
            'customer_service_email', 'telephone', 'address_line', 'locality',
            'region', 'postal_code', 'country'
        ]


class SEOConfigurationAdmin(ImportExportModelAdmin):
    resource_classes = [SEOConfigurationResource]
    list_display = ['full_name', 'created_on']
    date_hierarchy = 'created_on'
    readonly_fields = ['version']
    search_fields = ['author', 'company_name', 'keywords']
    actions = ['duplicate_container']
    fieldsets = [
        [
            'General',
            {
                'fields': ['author', 'company_name']
            }
        ],
        [
            'SEO',
            {
                'fields': ['keywords', 'description', 'theme_color']
            }
        ],
        [
            'Socials',
            {
                'fields': [
                    'linkedin',
                    'facebook',
                    'twitter',
                    'instagram',
                    'youtube',
                    'tiktok'
                ]
            }
        ]
    ]

    def duplicate_container(self, request, queryset):
        pass


class LegalBusinessAdmin(ImportExportModelAdmin):
    resource_classes = [LegalBusinessResource]
    list_display = ['legal_name', 'created_on']
    date_hierarchy = 'created_on'
    readonly_fields = ['version']
    search_fields = ['legal_name']
    actions = ['duplicate_container']

    fieldsets = [
        [
            'General',
            {
                'fields': [
                    'legal_name', 'siren',
                    'siret', 'ape', 'registration_place',
                    'company_type', 'founding_date'
                ]
            }
        ],
        [
            'Contact',
            {
                'fields': [
                    'general_email',
                    'customer_service_email', 'telephone', 'address_line',
                    'locality', 'region', 'postal_code', 'country'
                ]
            }
        ],
        [
            'Visuals',
            {
                'fields': ['logo']
            }
        ]
    ]

    def duplicate_container(self, request, queryset):
        pass


admin.site.register(SEOVersion, SEOConfigurationAdmin)
admin.site.register(LegalBusiness, LegalBusinessAdmin)
