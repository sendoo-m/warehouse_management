from home.admin import admin_site  # استيراد موقع الإدارة المخصص
from django.contrib import admin
from .models import *

class SalesReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'total_sales')  # Ensure these fields exist
    # search_fields = ['start_date', 'end_date']
    # list_filter = ['start_date', 'end_date']  # If 'created_at' doesn't exist, replace with valid fields

class PurchaseReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'total_purchases')  # Ensure these fields exist
    # search_fields = ['start_date', 'end_date']
    # list_filter = ['start_date', 'end_date']  # Replace 'created_at' with valid fields

class PaymentReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date')  # Ensure these fields exist
    # search_fields = ['start_date', 'end_date']
    # list_filter = ['start_date', 'end_date']  # Replace 'created_at' with valid fields

class RefundReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'total_refunds')  # Ensure these fields exist
    # search_fields = ['start_date', 'end_date']
    # list_filter = ['start_date', 'end_date']  # Replace 'created_at' with valid fields

class InventoryReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'total_inventory')  # Ensure these fields exist
    # search_fields = ['start_date', 'end_date']
    # list_filter = ['start_date', 'end_date']  # Replace 'created_at' with valid fields


admin_site.register(SalesReportView, SalesReportAdmin)
admin_site.register(PurchaseReport, PurchaseReportAdmin)
admin_site.register(PaymentReport, PaymentReportAdmin)
admin_site.register(RefundReport, RefundReportAdmin)
admin_site.register(InventoryReport, InventoryReportAdmin)
