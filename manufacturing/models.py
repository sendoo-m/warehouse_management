from django.db import models
from products.models import *
from materials.models import *
from inventory.models import *
from django.db import models
from products.models import FinishedProduct
from materials.models import RawProduct
from inventory.models import InventoryMovement, Warehouse

class ManufacturingProcess(models.Model):
    product = models.ForeignKey(RawProduct, on_delete=models.CASCADE)
    raw_materials_used = models.ManyToManyField(Material, through='MaterialUsage')
    quantity_produced = models.DecimalField(max_digits=10, decimal_places=2)
    production_date = models.DateTimeField(auto_now_add=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='manufacturing_warehouse')
    final_product_name = models.CharField(max_length=255, blank=True, null=True)

    def process_manufacturing(self):
        # خصم الكميات المستخدمة من المواد الخام
        for usage in self.materialusage_set.all():
            usage.material.deduct_quantity(usage.quantity_used)

        # خصم الكمية من المنتج الخام
        if self.product.stock_level >= self.quantity_produced:
            self.product.deduct_quantity(self.quantity_produced)
        else:
            raise ValueError(f"الكمية المتاحة من {self.product.name} غير كافية لإتمام العملية")

        # تحقق من وجود المنتج النهائي بناءً على الاسم
        try:
            finished_product = FinishedProduct.objects.get(name=self.final_product_name)
        except FinishedProduct.DoesNotExist:
            # إنشاء منتج نهائي جديد إذا لم يكن موجودًا
            finished_product = FinishedProduct.objects.create(
                name=self.final_product_name,
                sku=f"{self.product.sku}-FIN-{self.pk}",  # تعديل الـ SKU لتجنب التكرار
                weight=self.product.weight,
                price=self.product.price,
                stock_level=0,
            )

        # إضافة الكمية المنتجة إلى مخزون المنتج النهائي
        finished_product.add_to_stock(self.quantity_produced)

        # تسجيل حركة المخزون
        InventoryMovement.objects.create(
            product=finished_product,
            warehouse=self.warehouse,
            movement_type='IN',
            quantity=self.quantity_produced,
            description=f"Manufactured {self.quantity_produced} of {finished_product.name}",
        )

        self.save()

    def restore_materials(self):
        # استرجاع المواد الخام المستخدمة
        for usage in self.materialusage_set.all():
            usage.material.restore_quantity(usage.quantity_used)

        # استرجاع الكمية من المنتج الخام
        self.product.restore_quantity(self.quantity_produced)

        # إيجاد المنتج النهائي واسترجاع الكمية منه
        try:
            finished_product = FinishedProduct.objects.get(name=self.final_product_name)
        except FinishedProduct.DoesNotExist:
            return

        # خصم الكمية من المنتج النهائي إذا كانت متاحة
        if finished_product.stock_level >= self.quantity_produced:
            finished_product.deduct_from_stock(self.quantity_produced)

            # حذف المنتج النهائي إذا وصل المخزون إلى صفر
            if finished_product.stock_level == 0:
                finished_product.delete()
        else:
            raise ValueError(f"الكمية المتاحة من {finished_product.name} غير كافية لإتمام العملية.")




class MaterialUsage(models.Model):
    manufacturing_process = models.ForeignKey(ManufacturingProcess, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity_used} من {self.material.name} في {self.manufacturing_process.product.name}"
