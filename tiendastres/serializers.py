from rest_framework import serializers
from .models import Inventory, Order, Product, OrderProduct

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Product
        fields = ['id', 'sku', 'name']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Order
        fields = ['order_number']

class InventorySerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model  = Inventory
        fields = ['product', 'stock']
    
    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product = Product.objects.create(**product_data)
        inventory =  Inventory.objects.create(product=product, **validated_data)
        return inventory

class UpdateInventorySerializer(serializers.Serializer):
        stock = serializers.IntegerField()

class PurchaseProductSerializer(serializers.Serializer):

    product_id = serializers.IntegerField()
    total_products = serializers.IntegerField()

class OrderProductPurchaseSerializer(serializers.Serializer):

    products = serializers.ListField(
        child=PurchaseProductSerializer(),
        allow_empty=False
    )

class OrderProductSerializer(serializers.ModelSerializer):
    
    product = ProductSerializer()
    order = OrderSerializer()

    class Meta:
        model  = OrderProduct
        fields = ['product', 'order']
    
    def create(self, validated_data):
        product_data = validated_data.pop('product')
        order_data = validated_data.pop('order')

        product = Product.objects.create(**product_data)
        order = Order.objects.create(**order_data)

        order_procduct =  OrderProduct.objects.create(
            product = product,
            order = order
            **validated_data
        )
        return order_procduct
