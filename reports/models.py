from django.db import models
from django.db.models import Sum
from sales.models import SalesInvoice
from purchases.models import PurchaseInvoice
from payments.models import SalePayment, PurchasePayment, SaleRefund, PurchaseRefund
from inventory.models import InventoryMovement
from django.db.models import F, Sum, Count

class SalesReportView(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_quantity_sold = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Sales Report from {self.start_date} to {self.end_date}"

    @classmethod
    def generate(cls, start_date, end_date):
        # حساب إجمالي المبيعات بناءً على الكمية والسعر
        sales_invoices = SalesInvoice.objects.filter(invoice_date__range=[start_date, end_date])
        total_sales = sales_invoices.aggregate(total_sales=Sum(F('quantity') * F('sales_price') * (1 + F('vat_sale') / 100)))['total_sales'] or 0.00
        total_quantity_sold = sales_invoices.aggregate(Sum('quantity'))['quantity__sum'] or 0.00
        
        report = cls.objects.create(
            start_date=start_date,
            end_date=end_date,
            total_sales=total_sales,
            total_quantity_sold=total_quantity_sold
        )
        return report

class PurchaseReport(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_purchases = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_quantity_purchased = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Purchase Report from {self.start_date} to {self.end_date}"

    @classmethod
    def generate(cls, start_date, end_date):
        # Calculate total amount as the sum of (purchase_price * quantity * (1 + vat_percentage / 100))
        total_purchases = PurchaseInvoice.objects.filter(invoice_date__range=[start_date, end_date]) \
            .aggregate(total_purchases=Sum(F('purchase_price') * F('quantity') * (1 + F('vat_percentage') / 100)))['total_purchases'] or 0.00

        total_quantity_purchased = PurchaseInvoice.objects.filter(invoice_date__range=[start_date, end_date]) \
            .aggregate(Sum('quantity'))['quantity__sum'] or 0.00

        report = cls.objects.create(
            start_date=start_date,
            end_date=end_date,
            total_purchases=total_purchases,
            total_quantity_purchased=total_quantity_purchased
        )
        return report

class PaymentReport(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    net_payments = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Payment Report from {self.start_date} to {self.end_date}"

    @classmethod
    def generate(cls, start_date, end_date):
        # حساب إجمالي مدفوعات المبيعات
        total_sales_payments = SalePayment.objects.filter(payment_date__range=[start_date, end_date]) \
            .aggregate(total_sales_payments=Sum('payment_amount'))['total_sales_payments'] or Decimal('0.00')

        # حساب إجمالي مدفوعات الشراء
        total_purchase_payments = PurchasePayment.objects.filter(payment_date__range=[start_date, end_date]) \
            .aggregate(total_purchase_payments=Sum('payment_amount'))['total_purchase_payments'] or Decimal('0.00')

        # طباعة التحقق من القيم
        print(f"Total Sales Payments: {total_sales_payments}")
        print(f"Total Purchase Payments: {total_purchase_payments}")

        # حساب الفرق بين المدفوعات: المدفوعات من البيع مطروح منها المدفوعات للشراء
        net_payments = total_sales_payments - total_purchase_payments

        # طباعة الفرق للتحقق
        print(f"Net Payments: {net_payments}")

        # إنشاء التقرير
        report = cls.objects.create(
            start_date=start_date,
            end_date=end_date,
            net_payments=net_payments
        )
        return report


from decimal import Decimal

class InventoryReport(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_in_movements = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_out_movements = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Inventory Report from {self.start_date} to {self.end_date}"

    @property
    def total_inventory(self):
        # Ensure that total_in_movements and total_out_movements are both Decimal before subtraction
        return Decimal(self.total_in_movements) - Decimal(self.total_out_movements)

    @classmethod
    def generate(cls, start_date, end_date):
        total_in_movements = InventoryMovement.objects.filter(
            movement_type='IN', date__range=[start_date, end_date]
        ).aggregate(Sum('quantity'))['quantity__sum'] or Decimal('0.00')
        
        total_out_movements = InventoryMovement.objects.filter(
            movement_type='OUT', date__range=[start_date, end_date]
        ).aggregate(Sum('quantity'))['quantity__sum'] or Decimal('0.00')

        report = cls.objects.create(
            start_date=start_date,
            end_date=end_date,
            total_in_movements=Decimal(total_in_movements),
            total_out_movements=Decimal(total_out_movements)
        )
        return report



# class PaymentReport(models.Model):
#     start_date = models.DateField()
#     end_date = models.DateField()
#     total_sale_payments = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
#     total_purchase_payments = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

#     def __str__(self):
#         return f"Payment Report from {self.start_date} to {self.end_date}"

#     @property
#     def total_payments(self):
#         return self.total_sale_payments + self.total_purchase_payments

#     @classmethod
#     def generate(cls, start_date, end_date):
#         total_sale_payments = SalePayment.objects.filter(payment_date__range=[start_date, end_date]).aggregate(Sum('payment_amount'))['payment_amount__sum'] or 0.00
#         total_purchase_payments = PurchasePayment.objects.filter(payment_date__range=[start_date, end_date]).aggregate(Sum('payment_amount'))['payment_amount__sum'] or 0.00

#         report = cls.objects.create(
#             start_date=start_date,
#             end_date=end_date,
#             total_sale_payments=total_sale_payments,
#             total_purchase_payments=total_purchase_payments
#         )
#         return report


class RefundReport(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_sale_refunds = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_purchase_refunds = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Refund Report from {self.start_date} to {self.end_date}"

    @property
    def total_refunds(self):
        return self.total_sale_refunds + self.total_purchase_refunds

    @classmethod
    def generate(cls, start_date, end_date):
        total_sale_refunds = SaleRefund.objects.filter(refund_date__range=[start_date, end_date]).aggregate(Sum('refund_amount'))['refund_amount__sum'] or 0.00
        total_purchase_refunds = PurchaseRefund.objects.filter(refund_date__range=[start_date, end_date]).aggregate(Sum('refund_amount'))['refund_amount__sum'] or 0.00

        report = cls.objects.create(
            start_date=start_date,
            end_date=end_date,
            total_sale_refunds=total_sale_refunds,
            total_purchase_refunds=total_purchase_refunds
        )
        return report
