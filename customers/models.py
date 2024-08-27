from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    tax_number = models.CharField(max_length=50, blank=True, null=True)  # اختياري
    commercial_register = models.CharField(max_length=50, blank=True, null=True)  # اختياري
    phone_number = models.CharField(max_length=20)
    customer_code = models.CharField(max_length=20, unique=True)
    location_image = models.ImageField(upload_to='customer_images/', blank=True, null=True)  # حقل الصورة اختياري
    
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    tax_number = models.CharField(max_length=50, blank=True, null=True)  # اختياري
    commercial_register = models.CharField(max_length=50, blank=True, null=True)  # اختياري
    phone_number = models.CharField(max_length=20)
    company_code = models.CharField(max_length=20, unique=True)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)  # شعار الشركة
    
    def __str__(self):
        return self.name
