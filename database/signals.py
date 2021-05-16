from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import SkuData


@receiver(post_save, sender=SkuData)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update sku total on units update/create
    """
    instance.sku.update_units()


@receiver(post_delete, sender=SkuData)
def update_on_delete(sender, instance, **kwargs):
    """
    Update sku total on units delete
    """
    instance.sku.update_units()
