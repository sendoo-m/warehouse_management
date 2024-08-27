from django import forms
from .models import ManufacturingProcess, MaterialUsage

class ManufacturingProcessForm(forms.ModelForm):
    class Meta:
        model = ManufacturingProcess
        fields = ['product', 'quantity_produced', 'warehouse', 'final_product_name']
        labels = {
            'product': 'اسم المنتج الخام',
            'quantity_produced': 'الكمية المنتجة',
            'warehouse': 'المستودع',
            'final_product_name': 'الاسم النهائي للمنتج'
        }

class MaterialUsageForm(forms.ModelForm):
    class Meta:
        model = MaterialUsage
        fields = ['material', 'quantity_used']
        labels = {
            'material': 'المادة الخام',
            'quantity_used': 'الكمية المستخدمة'
        }
