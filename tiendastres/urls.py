#from django.conf.urls import url
from django.urls import path, include
from .views import (
    InventoryApiView,
    OrdersApiView,
    ProductApiView,
)

urlpatterns = [
    path('inventories/product/<int:product_id>', InventoryApiView.as_view()),
    path('products', ProductApiView.as_view()),
    path('orders', OrdersApiView.as_view()),
]