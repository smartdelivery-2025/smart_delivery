# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
from django.http import HttpResponse


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
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
            return redirect('register')

        # 🔥 BUSCAR EMPRESA POR CÓDIGO
        from companies.models import Company
        company = Company.objects.filter(code=company_code).first()

        if not company:
            messages.error(request, "Código de empresa inválido.")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            phone=phone,
            role='CLIENTE',
            company=company
        )

        messages.success(request, "Cuenta creada correctamente")
        return redirect('login')

    return render(request, 'register.html')




# Dashboards
@login_required
def admin_dashboard(request):
    return render(request, 'dashboard_content.html')

@login_required
def panel(request):
    return render(request, 'dashboard_base.html')

@login_required
def empresas(request):
    return HttpResponse("<h2>Empresas</h2>")

@login_required
def usuarios(request):
    return HttpResponse("<h2>Usuarios</h2>")

@login_required
def pedidos(request):
    return HttpResponse("<h2>Pedidos</h2>")

@login_required
def conductores(request):
    return HttpResponse("<h2>Conductores</h2>")

@login_required
def rutas(request):
    return HttpResponse("<h2>Rutas</h2>")

@login_required
def inventario(request):
    return HttpResponse("<h2>Inventario</h2>")

@login_required
def incidencias(request):
    return HttpResponse("<h2>Incidencias</h2>")

