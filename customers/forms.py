from django import forms
from .models import Customer, Company

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'tax_number', 'commercial_register', 'phone_number', 'customer_code', 'location_image')

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'address', 'tax_number', 'commercial_register', 'phone_number', 'company_code', 'company_logo')