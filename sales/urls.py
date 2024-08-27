from django.urls import path
from . import views

urlpatterns = [
    path('invoice/create/', views.create_sales_invoice, name='create_sales_invoice'),
    path('invoices/', views.sales_invoice_list, name='sales_invoice_list'),
    path('invoice/<int:invoice_id>/', views.sales_invoice_detail, name='sales_invoice_detail'),
]
