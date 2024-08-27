from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from materials.models import *
from django.core.paginator import Paginator
from django.forms import inlineformset_factory

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


@login_required
def create_manufacturing_process(request):
    if request.method == 'POST':
        form = ManufacturingProcessForm(request.POST)
        formset = MaterialUsageFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            manufacturing_process = form.save()
            formset.instance = manufacturing_process
            formset.save()
            
            # Explicitly call process_manufacturing
            manufacturing_process.process_manufacturing()

            return redirect('manufacturing_list')
    else:
        form = ManufacturingProcessForm()
        formset = MaterialUsageFormSet()

    return render(request, 'manufacturing/create_manufacturing_process.html', {
        'form': form,
        'formset': formset,
    })

# Define MaterialUsageFormSet
MaterialUsageFormSet = inlineformset_factory(
    ManufacturingProcess,
    MaterialUsage,
    form=MaterialUsageForm,
    extra=6,  # Adjust the number of extra forms to display
    can_delete=True  # Allow the forms to be deleted
)

@login_required
def manufacturing_list(request):
    manufacturing_processes = ManufacturingProcess.objects.all()
    price = RawProduct.objects.all()
    price_unit = Material.objects.all()
    paginator = Paginator(manufacturing_processes, 5)  # عرض 5 عمليات في كل صفحة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'manufacturing/manufacturing_list.html', {
        'page_obj': page_obj,
        'price': price,
        'price_unit': price_unit,
        'manufacturing_processes': page_obj.object_list,
    })
    
@login_required
def manufacturing_detail(request, process_id):
    # جلب تفاصيل عملية التصنيع باستخدام الـ ID
    manufacturing_process = get_object_or_404(ManufacturingProcess, pk=process_id)
    return render(request, 'manufacturing/manufacturing_detail.html', {'manufacturing_process': manufacturing_process})
