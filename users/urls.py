from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register_view,
    dashboard_redirect,
    admin_dashboard,
    supervisor_dashboard,
    driver_dashboard,
    client_dashboard
)

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='login.html',
        next_page='dashboard_redirect'
    ), name='login'),

    path('register/', register_view, name='register'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),

    path('dashboard-redirect/', dashboard_redirect, name='dashboard_redirect'),

    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('supervisor-dashboard/', supervisor_dashboard, name='supervisor_dashboard'),
    path('driver-dashboard/', driver_dashboard, name='driver_dashboard'),
    path('client-dashboard/', client_dashboard, name='client_dashboard'),
]