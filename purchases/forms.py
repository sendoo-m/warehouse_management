from django import forms
from .models import Vendors, PurchaseInvoice

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendors
        fields = ['name', 'address', 'tax_number', 'commercial_register', 'phone_number', 'vendors_code', 'vendors_logo']

class PurchaseInvoiceForm(forms.ModelForm):
    class Meta:
        model = PurchaseInvoice
        fields = ['vendor', 'material', 'quantity', 'purchase_price', 'vat_percentage']

######################### تجربتي ################################
from django import forms
from .models import MaterialInvoice

class MaterialInvoiceForm(forms.ModelForm):
    class Meta:
        model = MaterialInvoice
        fields = ('vendor', 'material_name', 'material_unit', 'quantity', 'unit_price', 'vat_material_purchase')