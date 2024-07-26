from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inventory

import logging

logger = logging.getLogger('django')

@receiver(post_save, sender=Inventory)
def check_product_stock(sender, instance, created, **kwargs):

    if instance.stock < 10:
        logger.info(f"Este producto {instance.product_id} tiene un stock inferior a 10")