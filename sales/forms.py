from django import forms
from .models import SalesInvoice

class SalesInvoiceForm(forms.ModelForm):
    class Meta:
        model = SalesInvoice
        fields = ['customer', 'finished_product', 'quantity', 'sales_price', 'vat_sale']
