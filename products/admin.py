from django.contrib import admin
from home.admin import admin_site  # استيراد موقع الإدارة المخصص

# Register your models here.
from django.contrib import admin
from products.models import *
from inventory.models import *
from orders.models import *

admin_site.register(ManufacturedProduct)
admin_site.register(Warehouse)
admin_site.register(InventoryMovement)
admin_site.register(Order)
admin_site.register(FinishedProduct)

