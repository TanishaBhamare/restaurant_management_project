from django.contrib import admin
from .models import Menu
from .models import MenuItem

@admin.register(Menu)
admin.site.register
class MenuAdmin(admin.ModelAdmin):
    list_display('name','price'):
    search_fields = ('name')
    list_filter = ('price')
