from django.contrib import admin
from .models import *
from home.admin import admin_site  # استيراد موقع الإدارة المخصص

# Register your models here.


admin_site.register(Material)
admin_site.register(RawProduct)
