from django.shortcuts import render, redirect, get_object_or_404
from .models import SalesInvoice
from .forms import SalesInvoiceForm
from inventory.models import Warehouse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate



@login_required
def create_sales_invoice(request):
    if request.method == 'POST':
        form = SalesInvoiceForm(request.POST)
        if form.is_valid():
            sales_invoice = form.save()

            # Try to get or create the default warehouse
            warehouse, created = Warehouse.objects.get_or_create(
                name="Default Warehouse",
                defaults={"description": "This is the default warehouse for all sales."}
            )

            try:
                sales_invoice.process_sale(warehouse=warehouse)
                return redirect('sales_invoice_list')
            except ValueError as e:
                form.add_error(None, str(e))  # Adding error to the form if stock is insufficient
    else:
        form = SalesInvoiceForm()

    return render(request, 'sales/create_sales_invoice.html', {
        'form': form,
    })

from django.core.paginator import Paginator

@login_required
def sales_invoice_list(request):
    invoices = SalesInvoice.objects.all()
    paginator = Paginator(invoices, 8)  # Show 8 invoices per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sales/sales_invoice_list.html', {'page_obj': page_obj})


from django.shortcuts import render, get_object_or_404
from sales.models import SalesInvoice
from customers.models import Company  # استيراد نموذج الشركة

@login_required
def sales_invoice_detail(request, invoice_id):
    invoice = get_object_or_404(SalesInvoice, pk=invoice_id)
    company = Company.objects.first()  # جلب أول سجل للشركة أو تخصيص الجلب بناءً على المتطلبات

    return render(request, 'sales/sales_invoice_detail.html', {
        'invoice': invoice,
        'company': company
    })

 