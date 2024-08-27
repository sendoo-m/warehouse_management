from django.db import models
from materials.models import RawProduct  # Safe import

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class InventoryMovement(models.Model):
    MOVEMENT_TYPES = (
        ('IN', 'إضافة'),
        ('OUT', 'خصم'),
    )
    # Do not import FinishedProduct here; import it inside methods
    product = models.ForeignKey('products.FinishedProduct', on_delete=models.CASCADE, null=True, blank=True)
    raw_material = models.ForeignKey(RawProduct, on_delete=models.CASCADE, null=True, blank=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # processed = models.BooleanField(default=False)

    def process_inventory(self):
        from products.models import FinishedProduct  # Local import to avoid circular dependency
        if self.movement_type == 'IN':
            if self.product:
                self.product.stock_level += self.quantity
                self.product.save()
            elif self.raw_material:
                self.raw_material.stock_level += self.quantity
                self.raw_material.save()
        elif self.movement_type == 'OUT':
            if self.product:
                self.product.stock_level -= self.quantity
                self.product.save()
            elif self.raw_material:
                self.raw_material.stock_level -= self.quantity
                self.raw_material.save()

    def __str__(self):
        return f"{self.movement_type} - {self.product or self.raw_material} - {self.quantity}"

