from django.contrib import admin
from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display('name','price'):
    search_fields = ('name')
    list_filter = ('price')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    search_fields = ('name',)
    list_filter = ('price',)