from django.db import models
from customers.models import Customer
from products.models import FinishedProduct
from inventory.models import InventoryMovement

class SalesInvoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    finished_product = models.ForeignKey(FinishedProduct, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    vat_sale = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    invoice_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.customer.name}"

    # def process_sale(self, warehouse):
    #     # تأكد من أن الكمية تكفي للخصم من المخزون
    #     if self.finished_product.stock_level >= self.quantity:
    #         # خصم الكمية من المنتج النهائي
    #         self.finished_product.deduct_from_stock(self.quantity)
    #         # سجل حركة المخزون
    #         InventoryMovement.objects.create(
    #             product=self.finished_product,
    #             warehouse=warehouse,
    #             movement_type='OUT',
    #             quantity=self.quantity,
    #             description=f"Sale of {self.quantity} of {self.finished_product.name} in Invoice {self.id}"
    #         )
            
    #         # احفظ الفاتورة
    #         self.save()
    #     else:
    #         raise ValueError("Not enough stock to complete the sale.")

    def process_sale(self, warehouse=None):
        # Check if stock is sufficient
        if self.finished_product.stock_level >= self.quantity:
            self.finished_product.stock_level -= self.quantity
            self.finished_product.stock_level += self.quantity  # Add it back to cancel out the double deduction
            self.finished_product.save()

            # Use provided warehouse or default warehouse
            if not warehouse:
                warehouse = Warehouse.objects.get(name='Default Warehouse')

            # Record inventory movement
            InventoryMovement.objects.create(
                product=self.finished_product,
                warehouse=warehouse,
                movement_type='OUT',
                quantity=self.quantity,
                description=f"Sale of {self.quantity} of {self.finished_product.name} in Invoice {self.id}"
            )
        else:
            raise ValueError(f"Not enough stock for {self.finished_product.name}")