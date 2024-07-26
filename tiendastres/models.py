from django.db import models

# Create your models here.

class Product(models.Model):

    sku = models.CharField(max_length=12, unique=True, blank=True)
    name = models.CharField(max_length=255, null=False)
    #stock = models.IntegerField(default=100)

    def __str__(self):
    	return self.name

class Inventory(models.Model):

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stock = models.IntegerField(default=100)

class Order(models.Model):

    order_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.order_number
    
    def save(self, *args, **kargs):
        if not self.order_number:
            super(Order, self).save()
            self.order_number = f'ORD{self.id:04d}'
            Order.objects.filter(id=self.id).update(
                order_number = self.order_number
            )
        else:
            super(Order, self).save(*args, **args)

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
