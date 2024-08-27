from django.urls import path
from . import views

urlpatterns = [
    path('treasury/', views.treasury_report, name='treasury_report'),
    path('customers_report/', views.customers_report, name='customers_report'),
    path('inventory/', views.inventory_report, name='inventory_report'),
    path('materials_report/', views.materials_report, name='materials_report'),
    path('manufacturing_report/', views.manufacturing_report, name='manufacturing_report'),
    path('generate_reports/', views.generate_reports, name='generate_reports'),
    path('reports/', views.report_view, name='report_view'),
    path('financial_report/', views.financial_report, name='financial_report'),
    
    
]
