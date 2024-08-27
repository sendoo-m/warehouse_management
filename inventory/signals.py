from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import transaction
from products.models import FinishedProduct
from inventory.models import InventoryMovement
from sales.models import SalesInvoice

import logging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=InventoryMovement)
def copy_to_finished_product(sender, instance, created, **kwargs):
    # Avoid infinite loops and ensure we only update stock for non-manufacturing movements
    if not created or not instance.product or 'Manufactured' in instance.description:
        return

    # Get the FinishedProduct
    finished_product = instance.product

    # Update the stock level based on the movement type
    if instance.movement_type == 'IN':
        finished_product.add_to_stock(instance.quantity)
    elif instance.movement_type == 'OUT':
        finished_product.deduct_from_stock(instance.quantity)


@receiver(post_delete, sender=InventoryMovement)
def restore_stock_on_delete(sender, instance, **kwargs):
    if instance.product:
        from products.models import FinishedProduct  # Localized import

        try:
            finished_product = instance.product

            logger.info(f"Restoring stock for {finished_product.name} after deletion of InventoryMovement")

            with transaction.atomic():
                if instance.movement_type == 'IN':
                    finished_product.deduct_from_stock(instance.quantity)
                elif instance.movement_type == 'OUT':
                    finished_product.add_to_stock(instance.quantity)

        except FinishedProduct.DoesNotExist:
            pass


@receiver(post_delete, sender=SalesInvoice)
def restore_finished_product_on_delete(sender, instance, **kwargs):
    """
    Restore finished product stock levels when a sales invoice is deleted.
    """
    finished_product = instance.finished_product

    with transaction.atomic():
        # Restore the stock level of the finished product
        finished_product.stock_level += instance.quantity  # Restore stock by the quantity sold
        finished_product.save()

        logger.info(f"Restored stock for {finished_product.name} after SalesInvoice deletion")

        # Find the related InventoryMovement for this sale and delete it
        InventoryMovement.objects.filter(
            product=finished_product,
            movement_type='OUT',
            quantity=instance.quantity,
            description=f"Sale of {instance.quantity} of {finished_product.name} in Invoice {instance.id}"
        ).delete()

