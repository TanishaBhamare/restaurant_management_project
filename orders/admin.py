from django.contrib import admin
from .models import Order,OrderItem

class OrderItemline(admin.TabularInLine):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','total_amount','order_status','created_at')
    list_filter = ('order_status','created_at')
    search_fields = ('customer__username',)
    inlines = [OrderItemline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','menu_item','quantity')   