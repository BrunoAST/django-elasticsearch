from django.contrib import admin

from demo.models import OfferedService


@admin.register(OfferedService)
class OfferedServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'description',
        'service_provider',
    )
    readonly_fields = ('id', 'service_provider',)
    search_fields = ('description', 'service_provider__full_name')
    autocomplete_fields = ('service_provider',)
