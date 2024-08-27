from django.shortcuts import render, redirect
from .models import Customer, Company
from .forms import CustomerForm, CompanyForm
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


@login_required
def customer_list(request):
    customers = Customer.objects.all()
    paginator = Paginator(customers, 10)  # حدد 10 عملاء لكل صفحة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customer/customer_list.html', {'page_obj': page_obj})

@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer/customer_form.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Customer
from sales.models import SalesInvoice
from payments.models import SalePayment
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from django.core.paginator import Paginator

@login_required
def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    sales = SalesInvoice.objects.filter(customer=customer)
    
    # حساب إجمالي الفاتورة لكل عملية بيع
    for sale in sales:
        sale.total_with_vat = sale.quantity * sale.sales_price * (1 + sale.vat_sale / 100)

    payments = SalePayment.objects.filter(customer=customer)
    total_purchases = sum(sale.total_with_vat for sale in sales)
    total_paid = sum(payment.payment_amount for payment in payments)
    balance = total_purchases - total_paid

    # إضافة التصفح (pagination)
    paginator = Paginator(sales, 5)  # عدد الفواتير لكل صفحة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # إضافة التصفح (pagination)
    paginator = Paginator(payments, 5)  # عدد الفواتير لكل صفحة
    page_number = request.GET.get('page')
    page_obj_payments = paginator.get_page(page_number)

    context = {
        'customer': customer,
        'page_obj': page_obj,  # استخدام الصفحة الحالية للفواتير
        'page_obj_payments': page_obj_payments,  # استخدام الصفحة الحالية للفواتير
        # 'payments': payments,
        'total_purchases': total_purchases,
        'total_paid': total_paid,
        'balance': balance,
    }
    
    return render(request, 'customer/customer_detail.html', context)



@login_required
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'customer/company_list.html', {'companies': companies})

@login_required
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'customer/company_form.html', {'form': form})

@login_required
def company_detail(request, pk):
    company = Company.objects.get(pk=pk)
    return render(request, 'customer/company_detail.html', {'company': company})