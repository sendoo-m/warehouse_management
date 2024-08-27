from django.shortcuts import render, get_object_or_404
from .models import *


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.


@login_required
def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'inventory/warehouse_list.html', {'warehouses': warehouses})

@login_required
def inventory_movements(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    movements = InventoryMovement.objects.filter(warehouse=warehouse)
    return render(request, 'inventory/inventory_movements.html', {'warehouse': warehouse, 'movements': movements})
