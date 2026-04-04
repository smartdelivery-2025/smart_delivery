# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
from django.http import HttpResponse
from companies.models import Company
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout


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


#login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('panel')  # 🔥 AQUÍ ESTÁ LA CLAVE
        else:
            messages.error(request, "Credenciales incorrectas")

    return render(request, 'login.html')






# Dashboards
@login_required
def admin_dashboard(request):
    return render(request, 'dashboard_content.html')

@login_required
def panel(request):
    return render(request, 'dashboard_base.html')

@login_required
def empresas(request):
    empresas = Company.objects.all()

    return render(request, 'empresas/empresas_content.html', {
        'empresas': empresas
    })

@login_required
def usuarios(request):
    users = User.objects.all()

    return render(request, 'usuarios/usuarios_content.html', {
        'users': users
    })

@csrf_exempt
def eliminar_empresa(request, id):
    if request.method == "POST":
        Company.objects.filter(id=id).delete()
        return JsonResponse({'success': True})


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

def logout_view(request):
    logout(request)
    return redirect('login')