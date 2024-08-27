from django.db import models

class RawProduct(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    description = models.TextField(blank=True)
    stock_level = models.IntegerField(default=0)  # كمية المخزون
    wastage_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

    
    def deduct_quantity(self, amount):
        if self.stock_level >= amount:
            self.stock_level -= amount
            self.save()
        else:
            raise ValueError('الكمية المتاحة من المنتج الخام غير كافية')

    def restore_quantity(self, amount):
        self.stock_level += amount
        self.save()

# class Material(models.Model):
#     name = models.CharField(max_length=100)
#     quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
#     unit = models.CharField(max_length=50)
#     price_per_unit = models.DecimalField(max_digits=10, decimal_places=3)
#     vat_material = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

#     def __str__(self):
#         return self.name

#     def deduct_quantity(self, amount):
#         """خصم الكمية المستخدمة من المخزون"""
#         if self.quantity >= amount:
#             self.quantity -= amount
#             self.save()
#             print(f"{amount} deducted from {self.name}, new quantity: {self.quantity}")

#         else:
#             raise ValueError(f"الكمية المتاحة من {self.name} غير كافية")

#     def restore_quantity(self, amount):
#         """استرجاع الكمية إلى المخزون عند حذف عملية التصنيع"""
#         self.quantity += amount
#         self.save()

import logging
from django.db import models
from django.db import transaction

class InsufficientQuantityError(Exception):
    pass

class Material(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    unit = models.CharField(max_length=50)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=3)
    vat_material = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

    @transaction.atomic
    def deduct_quantity(self, amount):
        """خصم الكمية المستخدمة من المخزون"""
        if self.quantity >= amount:
            self.quantity -= amount
            self.save()
            logging.info(f"{amount} deducted from {self.name}, new quantity: {self.quantity}")
        else:
            raise InsufficientQuantityError(f"الكمية المتاحة من {self.name} غير كافية")
    
    @transaction.atomic
    def restore_quantity(self, amount):
        """استرجاع الكمية إلى المخزون عند حذف عملية التصنيع"""
        self.quantity += amount
        self.save()
        logging.info(f"{amount} restored to {self.name}, new quantity: {self.quantity}")
