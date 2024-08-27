from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('PM', 'Project Manager'),
        ('WM', 'Warehouse Manager'),
        ('SS', 'Salesperson'),
        ('PS', 'Purchaseperson'),
    )
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    
    def is_project_manager(self):
        return self.role == 'PM'
    
    def is_warehouse_manager(self):
        return self.role == 'WM'
    
    def is_salesperson(self):
        return self.role == 'SS'
    
    def is_purchaseperson(self):
        return self.role == 'PS'
