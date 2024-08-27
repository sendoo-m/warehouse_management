from django.urls import path
from . import views

urlpatterns = [
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('warehouses/<int:warehouse_id>/movements/', views.inventory_movements, name='inventory_movements'),
]
