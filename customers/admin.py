from django.contrib import admin
from home.admin import admin_site  # استيراد موقع الإدارة المخصص

# Register your models here.

from django.contrib import admin
from .models import Customer, Company

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'customer_code', 'tax_number', 'commercial_register')
    search_fields = ('name', 'customer_code', 'phone_number')
    list_filter = ('tax_number', 'commercial_register')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'company_code', 'tax_number', 'commercial_register')
    search_fields = ('name', 'company_code', 'phone_number')
    list_filter = ('tax_number', 'commercial_register')

# تسجيل النماذج في لوحة الإدارة
admin_site.register(Customer, CustomerAdmin)
admin_site.register(Company, CompanyAdmin)

