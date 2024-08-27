from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseInvoice
from inventory.models import Warehouse, InventoryMovement

@receiver(post_save, sender=PurchaseInvoice)
def update_warehouse_inventory(sender, instance, created, **kwargs):
    if created:
        purchase_warehouse, created = Warehouse.objects.get_or_create(name="مخزن مشتريات الخامات")
        for item in instance.items.all():
            item.material.quantity += item.quantity
            item.material.save()

            InventoryMovement.objects.create(
                raw_material=item.material,
                warehouse=purchase_warehouse,
                movement_type='IN',
                quantity=item.quantity,
                description=f"شراء كمية {item.quantity} من {item.material.name} من الفاتورة {instance.id}"
            )
