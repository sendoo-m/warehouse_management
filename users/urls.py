from django.urls import path
from . import views

urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register_user, name='register_user'),
    # path('logout/', views.custom_logout, name='logout'),
    # path('list/', views.user_list, name='user_list'),
    # path('login/', views.login_view, name='login_view'),
]
