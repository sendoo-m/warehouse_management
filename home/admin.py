from django.contrib import admin

# Register your models here.

from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'لوحة التحكم الخاصة بك'
    site_title = 'إدارة الموقع'
    index_title = 'مرحبًا بك في لوحة التحكم'

    def get_app_list(self, request):
        app_order = [
            'home',  # التطبيق الخاص بالرئيسية
            'dashboard',  # التطبيق الخاص الاحصائيات
            'users',  # التطبيق الخاص بالمستخدمين
            'purchases',  # التطبيق الخاص بالمشتريات
            'customers',  # التطبيق الخاص بالعملاء
            'materials',  # التطبيق الخاص بالخامات
            'inventory',  # التطبيق الخاص بالمخزون
            'products',  # التطبيق الخاص بالمنتجات
            'manufacturing',  # التطبيق الخاص بالتصنيع
            'orders',  # التطبيق الخاص بالطلبات
            'sales',  # التطبيق الخاص بالمبيعات
            'payments',  # التطبيق الخاص بالمدفوعات
            'reports',  # التطبيق الخاص بالتقارير
            'notifications',  # التطبيق الخاص بالإشعارات
        ]
        app_list = super().get_app_list(request)
        ordered_app_list = sorted(app_list, key=lambda x: app_order.index(x['app_label']))
        return ordered_app_list

admin_site = MyAdminSite(name='myadmin')


