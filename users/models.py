from django.contrib.auth.models import AbstractUser
from django.db import models
from companies.models import Company


class User(AbstractUser):

    ROLE_CHOICES = (
        ('SUPERADMIN', 'Super Admin'),
        ('ADMIN', 'Admin'),
        ('SUPERVISOR', 'Supervisor'),
        ('CLIENTE', 'Cliente'),
        ('CONDUCTOR', 'Conductor'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.role}"

   


    
