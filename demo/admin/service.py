from django.contrib import admin

from demo.models import Service
from demo.models.expertise import Expertise


class ExpertiseInline(admin.TabularInline):
    model = Expertise
    extra = 0
    verbose_name = 'Expertise'
    verbose_name_plural = 'Expertises'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category_name',
    )
    list_select_related = (
        'category',
    )
    autocomplete_fields = ('category',)
    search_fields = ('name', 'category')
    inlines = (ExpertiseInline,)
    
    def category_name(self, obj):
        return obj.category.name
    