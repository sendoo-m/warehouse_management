from django.db import models
from inventory.models import Warehouse
# Create your models here.

class ManufacturedProduct(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('FILLET', 'Fillet'),
        ('PIECES', 'Pieces'),
        ('WHOLE', 'Whole Chicken'),
        ('MARINATED', 'Marinated Chicken'),
    ]

    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES, default='WHOLE')  # قيمة افتراضية
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)  # قيمة افتراضية للوزن
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # قيمة افتراضية للسعر
    description = models.TextField(blank=True)
    stock_level = models.IntegerField(default=0)  # قيمة افتراضية لمستوى المخزون
    wastage_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # قيمة افتراضية لنسبة الهالك

    def __str__(self):
        return f"{self.name} - {self.product_type}"


class FinishedProduct(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    description = models.TextField(blank=True)
    stock_level = models.IntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


    def add_to_stock(self, amount):
        """إضافة الكمية المنتجة إلى المخزون"""
        self.stock_level += amount
        self.save()

    def deduct_from_stock(self, amount):
        """خصم الكمية المباعة أو المستخدمة من المخزون"""
        if self.stock_level >= amount:
            self.stock_level -= amount
            self.save()
        else:
            raise ValueError('الكمية المتاحة من المنتج النهائي غير كافية')
