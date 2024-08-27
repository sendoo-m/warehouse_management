from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from .models import User

# @login_required
# def register_user(request):
#     if request.user.is_project_manager():
#         if request.method == 'POST':
#             form = CustomUserCreationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('user_list')
#         else:
#             form = CustomUserCreationForm()
#         return render(request, 'users/register.html', {'form': form})
#     else:
#         return redirect('home')

# @login_required
# def user_list(request):
#     if request.user.is_project_manager():
#         users = User.objects.all()
#         return render(request, 'users/user_list.html', {'users': users})
#     else:
#         return redirect('home')

# def custom_logout(request):
#     logout(request)
#     return redirect('home')

########################################################################
########################################################################
########################################################################
########################################################################

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def create_sales_invoice(request):
    if request.user.is_salesperson() or request.user.is_project_manager():
        return render(request, 'sales/create_sales_invoice.html')
    else:
        return redirect('home')

@login_required
def sales_invoice_list(request):
    if request.user.is_salesperson() or request.user.is_project_manager():
        return render(request, 'sales/sales_invoice_list.html')
    else:
        return redirect('home')

@login_required
def sales_invoice_detail(request, invoice_id):
    if request.user.is_salesperson() or request.user.is_project_manager():
        # تحميل تفاصيل الفاتورة بناءً على الـ invoice_id
        return render(request, 'sales/sales_invoice_detail.html', {'invoice_id': invoice_id})
    else:
        return redirect('home')

@login_required
def create_purchase_invoice(request):
    if request.user.is_purchaseperson() or request.user.is_project_manager():
        return render(request, 'purchases/create_purchase_invoice.html')
    else:
        return redirect('home')

@login_required
def purchase_invoice_list(request):
    if request.user.is_purchaseperson() or request.user.is_project_manager():
        return render(request, 'purchases/purchase_invoice_list.html')
    else:
        return redirect('home')

@login_required
def purchase_invoice_detail(request, invoice_id):
    if request.user.is_purchaseperson() or request.user.is_project_manager():
        return render(request, 'purchases/purchase_invoice_detail.html', {'invoice_id': invoice_id})
    else:
        return redirect('home')

@login_required
def treasury_report(request):
    if request.user.is_warehouse_manager() or request.user.is_project_manager():
        return render(request, 'reports/treasury_report.html')
    else:
        return redirect('home')

@login_required
def warehouse_list(request):
    if request.user.is_warehouse_manager() or request.user.is_project_manager():
        return render(request, 'warehouses/warehouse_list.html')
    else:
        return redirect('home')

def any_view(request):
    if request.user.is_project_manager():
        # Render the view for Project Manager
        return render(request, 'template_name.html')
    else:
        # Logic to check for other roles or redirect
        return redirect('home')


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')