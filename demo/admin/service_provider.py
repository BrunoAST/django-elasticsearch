from django.contrib import admin

from demo.models.offered_service import OfferedService
from demo.models.service_provider import ServiceProvider


class OfferedServiceInline(admin.TabularInline):
    model = OfferedService
    readonly_fields = ('id',)
    # autocomplete_fields = ('service',)
    extra = 1
    show_change_link = True


@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    inlines = (OfferedServiceInline,)
    list_display = (
        'id',
        'full_name',
        'email',
        'cellphone',
        'work_type',
    )
    search_fields = ('full_name', 'email', 'cellphone')
    