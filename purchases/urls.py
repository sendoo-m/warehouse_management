from django.urls import path
from . import views

urlpatterns = [

    ######### Vendors #########
    path('vendor/create/', views.create_vendor, name='create_vendor'),
    path('vendor/list/', views.vendor_list, name='vendor_list'),
    path('vendor/<int:vendor_id>/', views.vendor_details, name='vendor_details'),

    ######### purchase invoice #########
    path('invoice/create/', views.create_purchase_invoice, name='create_purchase_invoice'),
    path('invoice/list/', views.purchase_invoice_list, name='purchase_invoice_list'),
    path('invoice/<int:invoice_id>/', views.purchase_invoice_detail, name='purchase_invoice_detail'),

    ######### material  ##########
    path('material_invoices/', views.material_invoice_list, name='material_invoice_list'),
    path('material_invoices/create/', views.create_material_invoice, name='create_material_invoice'),
    path('material_invoices/<pk>/', views.material_invoice_detail, name='material_invoice_detail'),

]

