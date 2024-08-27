# from django.contrib import admin
# from .models import ManufacturingProcess

# class ManufacturingProcessAdmin(admin.ModelAdmin):
#     list_display = ('product', 'quantity_produced', 'production_date', 'warehouse')
#     search_fields = ('product__name', 'warehouse__name')
#     list_filter = ('production_date', 'warehouse')

# # تسجيل نموذج عملية التصنيع
# admin_site.register(ManufacturingProcess, ManufacturingProcessAdmin)

from django.contrib import admin
from .models import *
from home.admin import admin_site  # استيراد موقع الإدارة المخصص

class MaterialUsageInline(admin.TabularInline):
    model = MaterialUsage
    extra = 1  # عدد النماذج الإضافية التي ترغب في عرضها

class ManufacturingProcessAdmin(admin.ModelAdmin):
    list_display = ('final_product_name', 'product', 'quantity_produced', 'production_date', 'warehouse')
    search_fields = ('product__name', 'warehouse__name')
    list_filter = ('production_date', 'warehouse')
    inlines = [MaterialUsageInline]

admin_site.register(ManufacturingProcess, ManufacturingProcessAdmin)

