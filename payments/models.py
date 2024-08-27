from django.db import models
from customers.models import Customer
from purchases.models import Vendors

class PurchasePayment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('CREDIT_CARD', 'Credit Card'),
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('CASH', 'Cash on Delivery'),
    ]

    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('refunded', 'Refunded'),
    ])

    def __str__(self):
        return f"Payment of {self.payment_amount} by {self.vendor.name} - {self.payment_method}"

class SalePayment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('CREDIT_CARD', 'Credit Card'),
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('CASH', 'Cash on Delivery'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('refunded', 'Refunded'),
    ])

    def __str__(self):
        return f"Payment of {self.payment_amount} by {self.customer.name} - {self.payment_method}"

class PurchaseRefund(models.Model):
    REFUND_REASON_CHOICES = [
        ('RETURNED_GOODS', 'Returned Goods'),
        ('CANCELLED_ORDER', 'Cancelled Order'),
        ('OTHER', 'Other'),
    ]

    transaction = models.ForeignKey('PurchasePayment', on_delete=models.CASCADE, null=True, blank=True)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_date = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=20, choices=REFUND_REASON_CHOICES)
    description = models.TextField(default='No description provided')

    def __str__(self):
        return f"Refund of {self.refund_amount} for {self.transaction.vendor.name}"
        

class SaleRefund(models.Model):
    REFUND_REASON_CHOICES = [
        ('RETURNED_GOODS', 'Returned Goods'),
        ('CANCELLED_ORDER', 'Cancelled Order'),
        ('OTHER', 'Other'),
    ]

    transaction = models.ForeignKey('SalePayment', on_delete=models.CASCADE, null=True, blank=True)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_date = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=20, choices=REFUND_REASON_CHOICES)
    description = models.TextField(default='No description provided')

    def __str__(self):
        return f"Refund of {self.refund_amount} for {self.transaction.customer.name}"




from django.db import models

class Customerbalance(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)  # رصيد العميل

    def __str__(self):
        return self.name


class Vendorbalance(models.Model):
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)  # رصيد المورد

    def __str__(self):
        return self.name

