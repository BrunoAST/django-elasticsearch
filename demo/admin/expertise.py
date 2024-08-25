from django.contrib import admin

from demo.models import Expertise


@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'service_name'
    )
    list_select_related = (
        'service',
    )
    autocomplete_fields = ('service',)
    search_fields = ('name',)

    def service_name(self, obj):
        return obj.service.name
