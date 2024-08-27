# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.customer_list, name='customer_list'),  # لعرض قائمة العملاء
#     path('<int:customer_id>/', views.customer_detail, name='customer_detail'),  # لعرض تفاصيل العميل
#     path('company/', views.company_detail, name='company_detail'),  # لعرض تفاصيل الشركة
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<pk>/', views.customer_detail, name='customer_detail'),

    path('companies/', views.company_list, name='company_list'),
    path('companies/create/', views.company_create, name='company_create'),
    path('companies/<pk>/', views.company_detail, name='company_detail'),
]