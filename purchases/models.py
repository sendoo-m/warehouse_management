from django.db import models
from materials.models import Material
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from inventory.models import Warehouse, InventoryMovement
from materials.models import RawProduct  # استيراد RawProduct

class Vendors(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    tax_number = models.CharField(max_length=50, blank=True, null=True)  # اختياري
    commercial_register = models.CharField(max_length=50, blank=True, null=True)  # اختياري
    phone_number = models.CharField(max_length=20)
    vendors_code = models.CharField(max_length=20, unique=True)
    vendors_logo = models.ImageField(upload_to='vendors_logos/', blank=True, null=True)  # شعار المورد
    
    def __str__(self):
        return self.name


class PurchaseInvoice(models.Model):
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE, default=1)
    material = models.CharField(max_length=255, default="Default Material")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    vat_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    invoice_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.vendor.name}"

################ تجربتي  #############
class MaterialInvoice(models.Model):
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE, default=1)
    material_name = models.CharField(max_length=255, default="Default Material")
    material_unit = models.CharField(max_length=255, default="Unit Material")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    vat_material_purchase = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    invoice_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.vendor.name}"


@receiver(post_save, sender=PurchaseInvoice)
def update_warehouse_inventory(sender, instance, created, **kwargs):
    if created:
        # الحصول على المخزن أو إنشاؤه
        purchase_warehouse, created = Warehouse.objects.get_or_create(name="مخزن مشتريات الخامات")

        # إنشاء أو تحديث المنتج الخام في RawProduct
        raw_product, created = RawProduct.objects.get_or_create(
            name=instance.material,
            defaults={
                'sku': f"SKU-{instance.material[:5].upper()}-{instance.id}",
                'weight': 0,
                'price': instance.purchase_price,
                'stock_level': int(instance.quantity),
                'wastage_percentage': 0.0
            }
        )

        # إذا كان المنتج الخام موجوداً، تحديث المخزون
        if not created:
            raw_product.stock_level += int(instance.quantity)
            raw_product.save()

        # إنشاء حركة المخزون باستخدام RawProduct
        InventoryMovement.objects.create(
            raw_material=raw_product,  # استخدام RawProduct هنا
            warehouse=purchase_warehouse,
            movement_type='IN',
            quantity=instance.quantity,
            description=f"شراء كمية {instance.quantity} من {raw_product.name} من الفاتورة {instance.id}"
        )
