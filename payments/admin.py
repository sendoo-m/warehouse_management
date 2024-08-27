from django.contrib import admin
from payments.models import PurchasePayment, SalePayment, PurchaseRefund, SaleRefund
from home.admin import admin_site  # Import your custom admin site

# Define the admin for PurchasePayment
class PurchasePaymentAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'payment_amount', 'payment_method', 'payment_date', 'status')
    search_fields = ['vendor__name', 'transaction_id']
    list_filter = ['payment_method', 'status']

# Define the admin for SalePayment
class SalePaymentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'payment_amount', 'payment_method', 'payment_date', 'status')
    search_fields = ['customer__name', 'transaction_id']
    list_filter = ['payment_method', 'status']

# Define the admin for PurchaseRefund
class PurchaseRefundAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'refund_amount', 'refund_date', 'reason')
    search_fields = ['transaction__transaction_id']
    list_filter = ['reason']

# Define the admin for SaleRefund
class SaleRefundAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'refund_amount', 'refund_date', 'reason')
    search_fields = ['transaction__transaction_id']
    list_filter = ['reason']

# Register models with your custom admin site
admin_site.register(PurchasePayment, PurchasePaymentAdmin)
admin_site.register(SalePayment, SalePaymentAdmin)
admin_site.register(PurchaseRefund, PurchaseRefundAdmin)
admin_site.register(SaleRefund, SaleRefundAdmin)