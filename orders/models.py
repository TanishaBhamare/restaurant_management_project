from django.db import models
from django.contrib.auth.models import User

from menu.models import Menu

OEDER_STATUS_CHOICES = [
    ('PENDING' ,'Pending'),
    ('PROCESSING','Processing'),
    ('DELIVERED','Delivered'),
    ('CANCELLED','Cancelled'),
]

class Order(models.Model):
    customer = models.Foriegnkey(User, on_delete=models.CASCADE,related_name='orders')
    order_items = models.ManyToManyField(Menu, through='OrderItem')
    total_amount = models.DecimalField(max_digits=8,decimal_places=2)
    order_status = models.CharField(max_length=20,choices=ORDER_STATUS_CHOICES, default='PENDNG')
    created_at = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return f"Order{self.pk}-{self.customer.username}"