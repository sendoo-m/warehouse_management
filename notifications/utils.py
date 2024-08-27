from django.contrib.auth.models import User
from .models import Notification

def send_notification(user, message):
    Notification.objects.create(user=user, message=message)

def notify_sales_event(sale):
    # إرسال إشعار عند حدوث عملية بيع
    managers = User.objects.filter(groups__name__in=['Project Manager', 'Warehouse Manager'])
    for manager in managers:
        send_notification(manager, f"تمت عملية بيع جديدة: {sale}")

def notify_purchase_event(purchase):
    # إرسال إشعار عند حدوث عملية شراء
    managers = User.objects.filter(groups__name__in=['Project Manager', 'Warehouse Manager'])
    for manager in managers:
        send_notification(manager, f"تمت عملية شراء جديدة: {purchase}")

def notify_payment_event(payment):
    # إرسال إشعار عند حدوث عملية دفع
    managers = User.objects.filter(groups__name__in=['Project Manager', 'Warehouse Manager'])
    for manager in managers:
        send_notification(manager, f"تمت عملية دفع جديدة بمبلغ: {payment.amount} ريال")
