from django.urls import path
from . import views

urlpatterns = [
    path('purchase_payments/', views.list_purchase_payments, name='purchase_payment_list'),
    path('purchase_payments/create/', views.create_purchase_payment, name='purchase_payment_create'),
    path('purchase_payments/<pk>/', views.detail_purchase_payment, name='purchase_payment_detail'),

    path('sale_payments/', views.list_sale_payments, name='sale_payment_list'),
    path('sale_payments/create/', views.create_sale_payment, name='sale_payment_create'),
    path('sale_payments/<pk>/', views.detail_sale_payment, name='sale_payment_detail'),

    # Purchase Refunds
    path('purchase_refunds/', views.list_purchase_refunds, name='purchase_refund_list'),
    path('purchase_refunds/create/', views.create_purchase_refund, name='purchase_refund_create'),
    path('purchase_refunds/<pk>/', views.detail_purchase_refund, name='purchase_refund_detail'),

    # Sale Refunds
    path('sale_refunds/', views.list_sale_refunds, name='sale_refund_list'),
    path('sale_refunds/create/', views.create_sale_refund, name='sale_refund_create'),
    path('sale_refunds/<pk>/', views.detail_sale_refund, name='sale_refund_detail'),

    path('update_sale_payment/<int:payment_id>/', views.update_sale_payment_status, name='update_sale_payment_status'),
    path('update_purchase_payment/<int:payment_id>/', views.update_purchase_payment_status, name='update_purchase_payment_status'),
]