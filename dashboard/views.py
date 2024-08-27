from django.shortcuts import render
from reports.models import *
from customers.models import Customer
from products.models import FinishedProduct
from django.db.models import Sum, Count


# def dashboard_view(request):
#     # حساب بعض الإحصائيات الأساسية
#     total_sales = SalesReport.objects.aggregate(total=Sum('total_sales'))['total']
#     total_purchases = PurchaseReport.objects.aggregate(total=Sum('total_quantity_purchased'))['total']
#     total_inventory = InventoryMovement.objects.aggregate(total=Sum('quantity'))['total']
    
#     # حساب عدد العملاء
#     total_customers = Customer.objects.count()
    
#     # حساب كمية المنتجات المصنعة النهائية
#     total_finished_products = FinishedProduct.objects.aggregate(total=Sum('stock_level'))['total']

#     context = {
#         'total_sales': total_sales or 0,
#         'total_purchases': total_purchases or 0,
#         'total_inventory': total_inventory or 0,
#         'total_customers': total_customers or 0,
#         'total_finished_products': total_finished_products or 0,
#     }
    
#     return render(request, 'dashboard/dashboard.html', context)

from django.shortcuts import render
from django.utils.timezone import now
from django.db.models import Sum
from payments.models import SalePayment, PurchasePayment
from customers.models import Customer
from inventory.models import InventoryMovement
from products.models import FinishedProduct

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate



@login_required
def dashboard_view(request):
    # احصل على التاريخ الحالي
    today = now().date()

    # حساب إجمالي المدفوعات اليومية للمبيعات
    total_sales_payments = SalePayment.objects.filter(payment_date__date=today).aggregate(total=Sum('payment_amount'))['total']

    # حساب إجمالي المدفوعات اليومية للمشتريات
    total_purchase_payments = PurchasePayment.objects.filter(payment_date__date=today).aggregate(total=Sum('payment_amount'))['total']

    # حساب عدد العملاء
    total_customers = Customer.objects.count()

    # حساب كمية المنتجات المصنعة النهائية
    total_finished_products = FinishedProduct.objects.aggregate(total=Sum('stock_level'))['total']

    # حساب إجمالي المخزون (على سبيل المثال، جميع الحركات في المخزون)
    total_inventory = InventoryMovement.objects.aggregate(total=Sum('quantity'))['total']

    context = {
        'total_sales_payments': total_sales_payments or 0,
        'total_purchase_payments': total_purchase_payments or 0,
        'total_inventory': total_inventory or 0,
        'total_customers': total_customers or 0,
        'total_finished_products': total_finished_products or 0,
    }
    
    return render(request, 'dashboard/dashboard.html', context)
