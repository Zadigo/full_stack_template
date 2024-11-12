from django.contrib import admin

from careers import models


@admin.register(models.Job)
class JobsAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'description']


@admin.register(models.Illustration)
class IllustrationsAdmin(admin.ModelAdmin):
    list_display = ['url']
