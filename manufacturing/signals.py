from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import ManufacturingProcess

@receiver(pre_delete, sender=ManufacturingProcess)
def restore_materials_on_delete(sender, instance, **kwargs):
    instance.restore_materials()
