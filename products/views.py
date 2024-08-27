from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import ManufacturedProduct
@login_required
def product_list(request):
    products = ManufacturedProduct.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
@login_required
def product_detail(request, product_id):
    product = get_object_or_404(ManufacturedProduct, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
