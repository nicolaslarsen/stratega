from django.contrib import admin

# Register your models here.
from .models import Map, Strategy, Nade

class MapAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Map', {'fields': ['name', 'active_duty']}),
    ]
    list_display = ['name']

class StrategyAdmin(admin.ModelAdmin):
    search_fields = ['name']

class NadeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nade', 
            {'fields': 
                ['name',
                'map_name',
                'nade_type',
                'img_link',
                'img']
        })
    ]
    list_display = ['name']

admin.site.register(Map, MapAdmin)
admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Nade, NadeAdmin)
