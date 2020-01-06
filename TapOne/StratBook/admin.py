from django.contrib import admin

# Register your models here.
from .models import Map, Strategy

class MapAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Map Name', {'fields': ['name', 'active_duty']}),
    ]
    list_display = ['name']

class StrategyAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Map, MapAdmin)
admin.site.register(Strategy, StrategyAdmin)
