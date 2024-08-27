from django.shortcuts import render
from notifications.utils import notify_sales_event
from django.shortcuts import render
from .models import Notification

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


# Create your views here.


@login_required
def create_sales_order(request):
    # تنفيذ منطق إنشاء أمر البيع
    sale = SalesOrder.objects.create(...)  # مثال على عملية البيع
    # إرسال الإشعار
    notify_sales_event(sale)


@login_required
def notifications_list(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'notifications/notifications_list.html', {'notifications': notifications})

@login_required
def mark_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications_list')
