from django.contrib import admin
from .models import *
from home.admin import admin_site  # استيراد موقع الإدارة المخصص
from django.contrib import admin
from .models import Vendors, PurchaseInvoice

# إدارة الموردين
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'vendors_code', 'tax_number')
    search_fields = ('name', 'vendors_code')
    list_filter = ('tax_number', 'commercial_register')

# إدارة فواتير الشراء
class PurchaseInvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor', 'material', 'quantity', 'purchase_price', 'vat_percentage', 'invoice_date')
    search_fields = ('vendor__name', 'material')
    list_filter = ('invoice_date', 'vendor')


from .models import MaterialInvoice

class MaterialInvoiceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'material_name', 'material_unit', 'quantity', 'unit_price', 'vat_material_purchase', 'invoice_date')
    search_fields = ('vendor', 'material_name', 'material_unit')


# تسجيل النماذج في لوحة الإدارة
admin_site.register(Vendors, VendorAdmin)
admin_site.register(PurchaseInvoice, PurchaseInvoiceAdmin)
admin_site.register(MaterialInvoice, MaterialInvoiceAdmin)