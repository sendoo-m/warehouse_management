from django.contrib import admin
from home.admin import admin_site  # استيراد موقع الإدارة المخصص
from .models import *

# Register your models here.

# class SalesInvoiceInline(admin.TabularInline):
#     model = SalesInvoice
#     extra = 1  # Adjust this to the number of empty item slots you want to appear

class SalesInvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'invoice_date', 'quantity', 'sales_price')
    list_filter = ('vat_sale', 'invoice_date')
    search_fields = ('customer__name', 'id')
    # inlines = [SalesInvoiceInline]


admin_site.register(SalesInvoice, SalesInvoiceAdmin)