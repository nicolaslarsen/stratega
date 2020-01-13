from django.contrib import admin

# Register your models here.
from .models import Map, Strategy, Nade, Bullet

class MapAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Map', {'fields': ['name', 'active_duty']}),
    ]
    list_display = ['name']

class BulletInline(admin.StackedInline):
    model = Bullet
    extra = 1

class StrategyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [BulletInline]

class NadeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nade',
            {'fields':
                ['name',
                'map_name',
                'nade_type',
                'description',
                'img_link',
                'img']
        })
    ]
    list_display = ['name']

class BulletAdmin(admin.ModelAdmin):
    list_display = ['text']

admin.site.register(Map, MapAdmin)
admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Nade, NadeAdmin)
admin.site.register(Bullet, BulletAdmin)
