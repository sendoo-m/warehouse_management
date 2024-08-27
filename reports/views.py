from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import F, Sum, Count
from .models import *
from sales.models import *
from datetime import date
from django.core.paginator import Paginator
from django.utils.timezone import now
from payments.models import SalePayment, PurchasePayment

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate



@login_required
def treasury_report(request):
    # Get the current date
    today = now().date()

    # Query for total sales payments made today
    total_sales_payments = SalePayment.objects.filter(payment_date__date=today).aggregate(total=Sum('payment_amount'))['total'] or 0

    # Query for sale payments today
    sales_payments = SalePayment.objects.filter(payment_date__date=today)

    # Query for purchase payments today
    purchase_payments = PurchasePayment.objects.filter(payment_date__date=today)

    # Paginate sale payments
    sales_paginator = Paginator(sales_payments, 10)
    sales_page_number = request.GET.get('sales_page')
    sales_page_obj = sales_paginator.get_page(sales_page_number)

    # Paginate purchase payments
    purchases_paginator = Paginator(purchase_payments, 10)
    purchases_page_number = request.GET.get('purchases_page')
    purchases_page_obj = purchases_paginator.get_page(purchases_page_number)

    # Pass everything to the context
    context = {
        'total_sales_payments': total_sales_payments,
        'sales_page_obj': sales_page_obj,
        'purchases_page_obj': purchases_page_obj,
    }

    return render(request, 'reports/treasury_report.html', context)



@login_required
def inventory_report(request):
    inventory = InventoryMovement.objects.all().values('product__name').annotate(total_quantity=Sum('quantity'))
    return render(request, 'reports/inventory_report.html', {'inventory': inventory})

@login_required
def generate_reports(request):
    start_date = request.GET.get('start_date', datetime.today().strftime('%Y-%m-01'))
    end_date = request.GET.get('end_date', datetime.today().strftime('%Y-%m-%d'))

    sales_report = SalesReportView.generate(start_date, end_date)
    purchase_report = PurchaseReport.generate(start_date, end_date)
    payment_report = PaymentReport.generate(start_date, end_date)
    refund_report = RefundReport.generate(start_date, end_date)
    inventory_report = InventoryReport.generate(start_date, end_date)

    context = {
        'sales_report': sales_report,
        'purchase_report': purchase_report,
        'payment_report': payment_report,
        'refund_report': refund_report,
        'inventory_report': inventory_report,
    }

    return render(request, 'reports/report_summary.html', context)




from manufacturing.models import ManufacturingProcess  # Import your ManufacturingProcess model


@login_required
def manufacturing_report(request):
    # Aggregate manufacturing data
    total_products_manufactured = ManufacturingProcess.objects.aggregate(Sum('quantity_produced'))['quantity_produced__sum']
    manufacturing_processes = ManufacturingProcess.objects.all()
    # إضافة التصفح (pagination)

    paginator = Paginator(manufacturing_processes, 10)  # عدد الفواتير لكل صفحة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'total_products_manufactured': total_products_manufactured,
        'manufacturing_processes': manufacturing_processes,
    }
    return render(request, 'reports/manufacturing_report.html', context)

from django.db.models import Sum
from materials.models import RawProduct, Material

@login_required
def materials_report(request):
    # Aggregate material data for RawProduct
    total_raw_materials = RawProduct.objects.aggregate(Sum('stock_level'))['stock_level__sum'] or 0
    raw_materials = RawProduct.objects.all()

    # Aggregate material data for Material
    total_materials_used = Material.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
    materials = Material.objects.all()

    context = {
        'total_raw_materials': total_raw_materials,
        'raw_materials': raw_materials,
        'total_materials_used': total_materials_used,
        'materials': materials,
    }
    return render(request, 'reports/materials_report.html', context)


from customers.models import Customer

@login_required
def customers_report(request):
    # حساب عدد العملاء
    total_customers = Customer.objects.count()
    
    # جلب جميع العملاء
    customers = Customer.objects.all()

    context = {
        'total_customers': total_customers,
        'customers': customers,
    }
    return render(request, 'reports/customers_report.html', context)


import json
from django.shortcuts import render
from django.db.models import Sum, F
from decimal import Decimal
from sales.models import SalesInvoice
from purchases.models import PurchaseInvoice
from inventory.models import InventoryMovement

@login_required
def report_view(request):
    # حساب إجمالي المبيعات
    sales = SalesInvoice.objects.annotate(
        annotated_qty=F('quantity'), 
        annotated_total_amt=F('quantity') * F('sales_price')
    ).values('annotated_qty', 'annotated_total_amt')

    # حساب إجمالي المشتريات
    purchases = PurchaseInvoice.objects.annotate(
        annotated_qty=F('quantity'),  # استخدام الحقل الصحيح لـ 'quantity'
        annotated_total_amt=F('quantity') * F('purchase_price')  # حساب إجمالي المشتريات بناءً على الحقول الصحيحة
    ).values('annotated_qty', 'annotated_total_amt')

    # حساب إجمالي المدفوعات
    payments = SalePayment.objects.annotate(
        annotated_amount=F('payment_amount')
    ).values('annotated_amount')

    # حساب المخزون المتبقي باستخدام InventoryMovement
    inventory = InventoryMovement.objects.values('product__name').annotate(
        total_bal_qty=Sum('quantity')  # اجمع الكميات بناءً على الحقل الصحيح 'quantity'
    ).order_by('product__name')

    # تحويل قيم Decimal إلى float للتعامل مع JSON
    sales_data = [
        {'qty': float(sale['annotated_qty']), 'total_amt': float(sale['annotated_total_amt'])}
        for sale in sales
    ]
    purchases_data = [
        {'qty': float(purchase['annotated_qty']), 'total_amt': float(purchase['annotated_total_amt'])}
        for purchase in purchases
    ]
    payments_data = [
        {'amount': float(payment['annotated_amount'])}
        for payment in payments
    ]
    inventory_data = [
        {'product__name': inv['product__name'], 'total_bal_qty': float(inv['total_bal_qty'] or 0)}
        for inv in inventory
    ]

    context = {
        'sales': json.dumps(sales_data),
        'purchases': json.dumps(purchases_data),
        'payments': json.dumps(payments_data),
        'inventory': json.dumps(inventory_data),
    }

    return render(request, 'reports/report.html', context)


from django.db.models import Sum, DecimalField, F
from decimal import Decimal

@login_required
def financial_report(request):
    # Recalculate totals after any deletions
    total_sales = SalePayment.objects.aggregate(total_sales=Sum('payment_amount'))['total_sales'] or Decimal('0.00')
    total_purchases = PurchasePayment.objects.aggregate(total_purchases=Sum('payment_amount'))['total_purchases'] or Decimal('0.00')

    # حساب الفرق بين المدفوعات: المدفوعات من البيع مطروح منها المدفوعات للشراء
    net_payments = total_sales - total_purchases

    # تمرير القيم للقالب
    context = {
        'total_sales': total_sales,
        'total_purchases': total_purchases,
        'net_payments': net_payments,
    }

    return render(request, 'reports/financial_report.html', context)

