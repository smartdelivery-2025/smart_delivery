# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Vista de registro de clientes
def register_view(request):
    if request.method == "POST":
        company_code = request.POST.get('company_code')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            # Si quieres, puedes guardar company_code o phone en un perfil extendido
            messages.success(request, "Cuenta creada exitosamente. Inicia sesión.")
            return redirect('login')

    return render(request, 'register.html')


# Redirección del dashboard según tipo de usuario
@login_required
def dashboard_redirect(request):
    # Por simplicidad, todos van al admin_dashboard (ajustar según tu modelo de roles)
    return redirect('admin_dashboard')


# Dashboards
@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def supervisor_dashboard(request):
    return render(request, 'dashboard_base.html')  # plantilla temporal

@login_required
def driver_dashboard(request):
    return render(request, 'dashboard_base.html')  # plantilla temporal

@login_required
def client_dashboard(request):
    return render(request, 'dashboard_base.html')  # plantilla temporal