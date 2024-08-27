from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
]






















# from django.urls import path
# from . import views

#  urlpatterns = [
    # path('create/', views.create_manufacturing_process, name='create_manufacturing_process'),
    # path('', views.manufacturing_list, name='manufacturing_list'),  # صفحة قائمة التصنيع
    # path('<int:process_id>/', views.manufacturing_detail, name='manufacturing_detail'),  # صفحة التفاصيل لكل عملية

#     path('customers/', views.customer_list, name='customer_list'),
#     path('customers/create/', views.customer_create, name='customer_create'),
#     path('customers/<pk>/', views.customer_detail, name='customer_detail'),

#     path('companies/', views.company_list, name='company_list'),
#     path('companies/create/', views.company_create, name='company_create'),
#     path('companies/<pk>/', views.company_detail, name='company_detail'),

#     path('', views.customer_list, name='customer_list'),  # لعرض قائمة العملاء
#     path('<int:customer_id>/', views.customer_detail, name='customer_detail'),  # لعرض تفاصيل العميل
#     path('company/', views.company_detail, name='company_detail'),  # لعرض تفاصيل الشركة

#     path('sales/', views.sales_report, name='sales_report'),
#     path('inventory/', views.inventory_report, name='inventory_report'),
#     path('customer/<int:customer_id>/', views.customer_report, name='customer_report'),
#     path('materials_report/', views.materials_report, name='materials_report'),
#     path('manufacturing_report/', views.manufacturing_report, name='manufacturing_report'),

#     path('invoice/create/', views.create_sales_invoice, name='create_sales_invoice'),
#     path('invoices/', views.sales_invoice_list, name='sales_invoice_list'),
#     path('invoice/<int:invoice_id>/', views.sales_invoice_detail, name='sales_invoice_detail'),

#     path('', include('home.urls')),  # يمكننا إضافة روابط الصفحة الرئيسية لاحقًا
#     path('admin/', admin_site.urls),  # استخدام موقع الإدارة المخصص
#     # path('admin/', admin.site.urls),
#     path('users/', include('users.urls')),  # روابط تطبيق المستخدمين
#     path('products/', include('products.urls')),  # روابط تطبيق المنتجات
#     path('inventory/', include('inventory.urls')),  # روابط تطبيق المخزون
#     path('orders/', include('orders.urls')),  # روابط تطبيق الطلبات
#     path('manufacturing/', include('manufacturing.urls')),  # إضافة روابط التصنيع
#     path('customers/', include('customers.urls')),  # إضافة روابط التصنيع
#     path('payments/', include('payments.urls')),  # روابط الدفع
#     path('reports/', include('reports.urls')),  # روابط التقارير
#     path('dashboard/', include('dashboard.urls')),  # روابط لوحات المعلومات
#     path('notifications/', include('notifications.urls')),  # روابط الإشعارات
#     path('sales/', include('sales.urls')),  # روابط البيع
#     path('purchase/', include('purchases.urls')),  # روابط الشراء
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # رابط تسجيل الخروج

#     path('register/', views.register_user, name='register_user'),
#     path('logout/', views.custom_logout, name='logout'),
#     path('list/', views.user_list, name='user_list'),

#     ######### Vendors #########
#     path('vendor/create/', views.create_vendor, name='create_vendor'),
#     path('vendor/list/', views.vendor_list, name='vendor_list'),
#     path('vendor/<int:vendor_id>/', views.vendor_details, name='vendor_details'),

#     ######### purchase invoice #########
#     path('invoice/create/', views.create_purchase_invoice, name='create_purchase_invoice'),
#     path('invoice/list/', views.purchase_invoice_list, name='purchase_invoice_list'),
#     path('invoice/<int:invoice_id>/', views.purchase_invoice_detail, name='purchase_invoice_detail'),

#     path('', views.product_list, name='product_list'),
#     path('<int:product_id>/', views.product_detail, name='product_detail'),

#     path('purchase_payments/', views.list_purchase_payments, name='purchase_payment_list'),
#     path('purchase_payments/create/', views.create_purchase_payment, name='purchase_payment_create'),
#     path('purchase_payments/<pk>/', views.detail_purchase_payment, name='purchase_payment_detail'),

#     path('sale_payments/', views.list_sale_payments, name='sale_payment_list'),
#     path('sale_payments/create/', views.create_sale_payment, name='sale_payment_create'),
#     path('sale_payments/<pk>/', views.detail_sale_payment, name='sale_payment_detail'),

#     # Purchase Refunds
#     path('purchase_refunds/', views.list_purchase_refunds, name='purchase_refund_list'),
#     path('purchase_refunds/create/', views.create_purchase_refund, name='purchase_refund_create'),
#     path('purchase_refunds/<pk>/', views.detail_purchase_refund, name='purchase_refund_detail'),

#     # Sale Refunds
#     path('sale_refunds/', views.list_sale_refunds, name='sale_refund_list'),
#     path('sale_refunds/create/', views.create_sale_refund, name='sale_refund_create'),
#     path('sale_refunds/<pk>/', views.detail_sale_refund, name='sale_refund_detail'),
#     path('create/', views.create_manufacturing_process, name='create_manufacturing_process'),
#     path('', views.manufacturing_list, name='manufacturing_list'),  # صفحة قائمة التصنيع
#     path('<int:process_id>/', views.manufacturing_detail, name='manufacturing_detail'),  # صفحة التفاصيل لكل عملية
#     path('warehouses/', views.warehouse_list, name='warehouse_list'),
#     path('warehouses/<int:warehouse_id>/movements/', views.inventory_movements, name='inventory_movements'),
# ]

