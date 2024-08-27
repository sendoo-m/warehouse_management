from django import forms
from .models import PurchasePayment, SalePayment, PurchaseRefund, SaleRefund

class PurchasePaymentForm(forms.ModelForm):
    class Meta:
        model = PurchasePayment
        fields = ['vendor', 'payment_amount', 'payment_method', 'transaction_id']

class SalePaymentForm(forms.ModelForm):
    class Meta:
        model = SalePayment
        fields = ['customer', 'payment_amount', 'payment_method', 'transaction_id']

class PurchaseRefundForm(forms.ModelForm):
    class Meta:
        model = PurchaseRefund
        fields = ['transaction', 'refund_amount', 'reason', 'description']

class SaleRefundForm(forms.ModelForm):
    class Meta:
        model = SaleRefund
        fields = ['transaction', 'refund_amount', 'reason', 'description']
