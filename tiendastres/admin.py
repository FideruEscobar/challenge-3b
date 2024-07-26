from django.contrib import admin
from .models import (
    Inventory,
    Order,
    Product,
    OrderProduct,
)

# Register your models here.
admin.site.register(Order)
admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(OrderProduct)
