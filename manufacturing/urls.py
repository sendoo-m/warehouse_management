from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_manufacturing_process, name='create_manufacturing_process'),
    path('', views.manufacturing_list, name='manufacturing_list'),  # صفحة قائمة التصنيع
    path('<int:process_id>/', views.manufacturing_detail, name='manufacturing_detail'),  # صفحة التفاصيل لكل عملية
]