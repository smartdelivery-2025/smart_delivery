from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, admin_dashboard
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('register/', register_view, name='register'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),

    path('panel/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('panel/', views.panel, name='panel'),
    path('panel/empresas/', views.empresas, name='empresas'),
    path('panel/usuarios/', views.usuarios, name='usuarios'),
    path('panel/pedidos/', views.pedidos, name='pedidos'),
    path('panel/conductores/', views.conductores, name='conductores'),
    path('panel/rutas/', views.rutas, name='rutas'),
    path('panel/inventario/', views.inventario, name='inventario'),
    path('panel/incidencias/', views.incidencias, name='incidencias'),
]