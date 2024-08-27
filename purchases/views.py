from django.shortcuts import render, redirect, get_object_or_404
from .forms import VendorForm, PurchaseInvoiceForm
from .models import Vendors, PurchaseInvoice
from django.core.paginator import Paginator
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


# إنشاء بائع جديد
@login_required
def create_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'purchases/create_vendor.html', {'form': form})

# قائمة البائعين
@login_required
def vendor_list(request):
    vendors = Vendors.objects.all()
    return render(request, 'purchases/vendor_list.html', {'vendors': vendors})

# تفاصيل البائع
from django.shortcuts import render, get_object_or_404
from .models import Vendors
from django.core.paginator import Paginator
from payments.models import PurchasePayment

@login_required
def vendor_details(request, vendor_id):
    # الحصول على تفاصيل المورد
    vendor = get_object_or_404(Vendors, pk=vendor_id)
    
    # جلب الفواتير المرتبطة بالمورد
    invoices = PurchaseInvoice.objects.filter(vendor=vendor)
    
    # حساب إجمالي الفاتورة لكل عملية شراء
    for invoice in invoices:
        invoice.total_with_vat = invoice.quantity * invoice.purchase_price * (1 + invoice.vat_percentage / 100)

    # جلب المدفوعات المرتبطة بالمورد
    payments = PurchasePayment.objects.filter(vendor=vendor)
     
    # حساب الإجماليات
    total_invoices = sum(invoice.total_with_vat for invoice in invoices)
    total_paid = sum(payment.payment_amount for payment in payments)
    balance = total_invoices - total_paid
    
    # إضافة التصفح (pagination) للفواتير
    paginator = Paginator(invoices, 10)  # عدد الفواتير لكل صفحة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # تمرير البيانات إلى القالب
    context = {
        'vendor': vendor,
        'page_obj': page_obj,  # قائمة الفواتير الحالية مع التصفح
        'payments': payments,
        'total_invoices': total_invoices,
        'total_paid': total_paid,
        'balance': balance,
    }
    
    return render(request, 'purchases/vendor_details.html', context)


##################################################################################################

@login_required
def create_purchase_invoice(request):
    if request.method == 'POST':
        form = PurchaseInvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            return redirect('purchase_invoice_list')  # يتم توجيه المستخدم إلى صفحة قائمة الفواتير بعد الحفظ
    else:
        form = PurchaseInvoiceForm()

    return render(request, 'purchases/create_purchase_invoice.html', {'form': form})



#def purchase_invoice_list(request):
#     invoices = PurchaseInvoice.objects.all()  # جلب جميع الفواتير من قاعدة البيانات
#     return render(request, 'purchases/purchase_invoice_list.html', {'invoices': invoices})

@login_required
def purchase_invoice_list(request):
    invoices = PurchaseInvoice.objects.all()
    
    # حساب المبلغ الإجمالي لكل فاتورة
    for invoice in invoices:
        total_amount = (invoice.purchase_price * invoice.quantity) + ((invoice.purchase_price * invoice.quantity) * (invoice.vat_percentage / 100))
        invoice.total_amount = total_amount  # إضافة الحقل إلى كل فاتورة
        invoice.total_amount = round(total_amount, 2)  # تقريب إلى رقمين عشريين

    # تحديد عدد الفواتير لكل صفحة
    paginator = Paginator(invoices, 6)  # عرض 8 فواتير لكل صفحة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        
    return render(request, 'purchases/purchase_invoice_list.html', {'page_obj': page_obj})


from django.shortcuts import render, get_object_or_404
from .models import PurchaseInvoice
from customers.models import Company

@login_required
def purchase_invoice_detail(request, invoice_id):
    invoice = get_object_or_404(PurchaseInvoice, pk=invoice_id)
    # افترض أنك تخزن بيانات الشركة باستخدام كود معين
    company = get_object_or_404(Company)  # تعديل, company_code="YOUR_COMPANY_CODE" لإحضار بيانات الشركة
    return render(request, 'purchases/purchase_invoice_detail.html', {
        'invoice': invoice,
        'company': company  # إضافة بيانات الشركة لتمريرها إلى القالب
    })


########################################################## تجربتي #######################3
from django.shortcuts import render, redirect
from .models import MaterialInvoice
from .forms import MaterialInvoiceForm

#def create_material_invoice(request):
#     if request.method == 'POST':
#         form = MaterialInvoiceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('material_invoice_list')
#     else:
#         form = MaterialInvoiceForm()
#     return render(request, 'create_material_invoice.html', {'form': form})

@login_required
def material_invoice_list(request):
    invoices = MaterialInvoice.objects.all()
    
    # حساب المبلغ الإجمالي لكل فاتورة
    for invoice in invoices:
        total_amount = (invoice.unit_price * invoice.quantity) + ((invoice.unit_price * invoice.quantity) * (invoice.vat_material_purchase / 100))
        invoice.total_amount = total_amount  # إضافة الحقل إلى كل فاتورة
        invoice.total_amount = round(total_amount, 2)  # تقريب إلى رقمين عشريين

    # تحديد عدد الفواتير لكل صفحة
    paginator = Paginator(invoices, 6)  # عرض 8 فواتير لكل صفحة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    return render(request, 'purchases/material_invoice_list.html', {'page_obj': page_obj})

from django.shortcuts import get_object_or_404, render

@login_required
def material_invoice_detail(request, pk):
    # Get the MaterialInvoice object based on the pk passed to the view
    invoice = get_object_or_404(MaterialInvoice, pk=pk)

    # Assuming you're retrieving the company data, adjust this based on your logic
    # If you have a specific company_code or want to fetch the first company record, adjust accordingly
    company = get_object_or_404(Company)  # Adjust logic if you need a specific company
    
    # Pass the invoice and company to the template
    return render(request, 'purchases/material_invoice_detail.html', {
        'invoice': invoice,
        'company': company
    })



#def create_material_invoice(request):
#     if request.method == 'POST':
#         form = MaterialInvoiceForm(request.POST)
#         if form.is_valid():
#             invoice = form.save(commit=False)
#             material_name = invoice.material_name
#             material_unit = invoice.material_unit
#             quantity = invoice.quantity

#             # Check if the material already exists
#             material, created = Material.objects.get_or_create(name=material_name, unit=material_unit)

#             # Update the material's quantity
#             material.quantity += quantity
#             material.save()

#             invoice.save()  # Save the invoice now that the material is updated
#             return redirect('material_invoice_list')
#     else:
#         form = MaterialInvoiceForm()
#     return render(request, 'purchases/create_material_invoice.html', {'form': form})

from django.shortcuts import render, redirect
from .models import MaterialInvoice, Material
from .forms import MaterialInvoiceForm  # Assuming you have a form for MaterialInvoice

@login_required
def create_material_invoice(request):
    if request.method == 'POST':
        form = MaterialInvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            material_name = invoice.material_name
            material_unit = invoice.material_unit
            quantity = invoice.quantity

            try:
                # Check if the material already exists
                material, created = Material.objects.get_or_create(name=material_name, unit=material_unit)
                
                # Update the material's quantity if it exists, otherwise create a new one
                material.quantity += quantity
                material.save()

                # Save the invoice now that the material is updated
                invoice.save()
                
                return redirect('material_invoice_list')  # Redirect after saving
            except Exception as e:
                form.add_error(None, f"Error updating material: {e}")
    else:
        form = MaterialInvoiceForm()

    return render(request, 'purchases/create_material_invoice.html', {'form': form})
