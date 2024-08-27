from django.contrib import admin
from .models import User
from home.admin import admin_site  # استيراد موقع الإدارة المخصص

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')

admin_site.register(User, CustomUserAdmin)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# class CustomUserAdmin(UserAdmin):
#     # تخصيص الحقول التي ستظهر في صفحة قائمة المستخدمين
#     list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')

#     # تخصيص الحقول التي ستظهر في صفحة تفاصيل المستخدم
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('role',)}),
#     )

#     # تخصيص الحقول التي تظهر عند إنشاء مستخدم جديد
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('role',)}),
#     )

# # تسجيل النموذج المخصص
# admin.site.register(User, CustomUserAdmin)
