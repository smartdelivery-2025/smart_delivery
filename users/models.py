from django.db import models
from django.contrib.auth.models import AbstractUser
from companies.models import Company

class User(AbstractUser):
    ROLE_CHOICES = [
        ('SUPERADMIN', 'Super Admin'),
        ('ADMIN', 'Admin'),
        ('SUPERVISOR', 'Supervisor'),
        ('CONDUCTOR', 'Conductor'),
        ('CLIENTE', 'Cliente'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)

    # 🔥 RELACIÓN CON EMPRESA
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    
