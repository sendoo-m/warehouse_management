from django.contrib import admin
from .models import Notification
from home.admin import admin_site  # استيراد موقع الإدارة المخصص

# Register your models here.


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('user__username', 'message')

admin_site.register(Notification, NotificationAdmin)
