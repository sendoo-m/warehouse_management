from django.shortcuts import render, redirect
from .models import PurchasePayment, SalePayment, PurchaseRefund, SaleRefund
from .forms import PurchasePaymentForm, SalePaymentForm, SaleRefundForm, PurchaseRefundForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate



@login_required
def create_purchase_payment(request):
    if request.method == 'POST':
        form = PurchasePaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/payments/purchase_payments/')
    else:
        form = PurchasePaymentForm()
    return render(request, 'payments/purchase_payment_form.html', {'form': form})

@login_required
def list_purchase_payments(request):
    purchase_payments = PurchasePayment.objects.all()
    return render(request, 'payments/purchase_payment_list.html', {'purchase_payments': purchase_payments})

@login_required
def detail_purchase_payment(request, pk):
    purchase_payment = PurchasePayment.objects.get(pk=pk)
    return render(request, 'payments/purchase_payment_detail.html', {'purchase_payment': purchase_payment})

@login_required
def create_sale_payment(request):
    if request.method == 'POST':
        form = SalePaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/payments/sale_payments/')
    else:
        form = SalePaymentForm()
    return render(request, 'payments/sale_payment_form.html', {'form': form})

@login_required
def list_sale_payments(request):
    sale_payments = SalePayment.objects.all()
    return render(request, 'payments/sale_payment_list.html', {'sale_payments': sale_payments})

@login_required
def detail_sale_payment(request, pk):
    sale_payment = SalePayment.objects.get(pk=pk)
    return render(request, 'payments/sale_payment_detail.html', {'sale_payment': sale_payment})

# def create_purchase_refund(request):
#     if request.method == 'POST':
#         form = PurchaseRefundForm(request.POST)
#         if form.is_valid():
#             refund = form.save(commit=False)
#             transaction = ...  # Get the PurchasePayment transaction object
#             refund.transaction = transaction
#             refund.save()
#             return redirect('/payments/purchase_refunds/')
#     else:
#         form = PurchaseRefundForm()
#     return render(request, 'payments/purchase_refund_form.html', {'form': form})

@login_required
def list_purchase_refunds(request):
    refunds = PurchaseRefund.objects.all()
    return render(request, 'payments/purchase_refund_list.html', {'refunds': refunds})

@login_required
def detail_purchase_refund(request, pk):
    refund = PurchaseRefund.objects.get(pk=pk)
    return render(request, 'payments/purchase_refund_detail.html', {'refund': refund})


# def create_sale_refund(request):
#     if request.method == 'POST':
#         form = SaleRefundForm(request.POST)
#         if form.is_valid():
#             refund = form.save(commit=False)
#             transaction = ...  # Get the SalePayment transaction object
#             refund.transaction = transaction
#             refund.save()
#             return redirect('/payments/sale_refunds/')
#     else:
#         form = SaleRefundForm()
#     return render(request, 'payments/sale_refund_form.html', {'form': form})

@login_required
def list_sale_refunds(request):
    refunds = SaleRefund.objects.all()
    return render(request, 'payments/sale_refund_list.html', {'refunds': refunds})

@login_required
def detail_sale_refund(request, pk):
    refund = SaleRefund.objects.get(pk=pk)
    return render(request, 'payments/sale_refund_detail.html', {'refund': refund})



from django.shortcuts import get_object_or_404, redirect
from decimal import Decimal

@login_required
def create_purchase_refund(request):
    if request.method == 'POST':
        form = PurchaseRefundForm(request.POST)
        if form.is_valid():
            refund = form.save(commit=False)
            transaction = get_object_or_404(PurchasePayment, id=request.POST.get('transaction_id'))
            refund.transaction = transaction

            # تحديث رصيد المورد في جدول Vendorbalance
            vendor_balance = get_object_or_404(Vendorbalance, vendor=transaction.vendor)
            vendor_balance.balance += refund.refund_amount
            vendor_balance.save()

            refund.save()
            return redirect('/payments/purchase_refunds/')
    else:
        form = PurchaseRefundForm()
    return render(request, 'payments/purchase_refund_form.html', {'form': form})


@login_required
def create_sale_refund(request):
    if request.method == 'POST':
        form = SaleRefundForm(request.POST)
        if form.is_valid():
            refund = form.save(commit=False)
            try:
                # الحصول على المعاملة بناءً على ID المختار من النموذج
                transaction = SalePayment.objects.get(id=request.POST.get('transaction'))
                refund.transaction = transaction
                refund.save()
                return redirect('sale_refund_list')
            except SalePayment.DoesNotExist:
                form.add_error('transaction', 'لم يتم العثور على عملية الدفع.')
    else:
        form = SaleRefundForm()

    return render(request, 'payments/sale_refund_form.html', {'form': form})







from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from payments.models import SalePayment, PurchasePayment
from django.urls import reverse

# def update_sale_payment_status(request, payment_id):
#     sale_payment = get_object_or_404(SalePayment, id=payment_id)

#     if request.method == 'POST':
#         new_status = request.POST.get('status')
#         sale_payment.status = new_status
#         sale_payment.save()
#         return redirect('treasury_report')  # أو يمكن تحويل المستخدم إلى صفحة أخرى

#     return render(request, 'payments/update_sale_payment.html', {'sale_payment': sale_payment})

# def update_purchase_payment_status(request, payment_id):
#     purchase_payment = get_object_or_404(PurchasePayment, id=payment_id)

#     if request.method == 'POST':
#         new_status = request.POST.get('status')
#         purchase_payment.status = new_status
#         purchase_payment.save()
#         return redirect('treasury_report')  # أو يمكن تحويل المستخدم إلى صفحة أخرى

#     return render(request, 'payments/update_purchase_payment.html', {'purchase_payment': purchase_payment})
from .models import Customerbalance, Vendorbalance, SalePayment, PurchasePayment
from django.shortcuts import get_object_or_404, render, redirect

@login_required
def update_sale_payment_status(request, payment_id):
    sale_payment = get_object_or_404(SalePayment, id=payment_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')

        if new_status == 'refunded' and sale_payment.status != 'refunded':
            # حاول العثور على رصيد العميل، وإذا لم يتم العثور عليه، قم بإنشائه
            customer_balance, created = Customerbalance.objects.get_or_create(customer=sale_payment.customer)
            customer_balance.balance += sale_payment.payment_amount
            customer_balance.save()

        sale_payment.status = new_status
        sale_payment.save()
        return redirect('treasury_report')

    return render(request, 'payments/update_sale_payment.html', {'sale_payment': sale_payment})

@login_required
def update_purchase_payment_status(request, payment_id):
    purchase_payment = get_object_or_404(PurchasePayment, id=payment_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')

        if new_status == 'refunded' and purchase_payment.status != 'refunded':
            # حاول العثور على رصيد المورد، وإذا لم يتم العثور عليه، قم بإنشائه
            vendor_balance, created = Vendorbalance.objects.get_or_create(vendor=purchase_payment.vendor)
            vendor_balance.balance += purchase_payment.payment_amount
            vendor_balance.save()

        purchase_payment.status = new_status
        purchase_payment.save()
        return redirect('treasury_report')

    return render(request, 'payments/update_purchase_payment.html', {'purchase_payment': purchase_payment})
