from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import User

@receiver(post_migrate)
def create_default_admin(sender, **kwargs):
    if not User.objects.filter(email='administrador@smartdelivery.com').exists():
        User.objects.create_user(
            username='admin',
            email='administrador@smartdelivery.com',
            password='Admin123456!',
            role='SUPERADMIN',
            is_staff=True,
            is_superuser=True
        )