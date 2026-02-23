from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import User


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            email=email,
            phone=phone,
            password=password1,
            role='CLIENTE'
        )

        login(request, user)
        return redirect('dashboard_redirect')

    return render(request, 'register.html')


def dashboard_redirect(request):
    if request.user.role in ['SUPERADMIN', 'ADMIN']:
        return redirect('admin_dashboard')
    elif request.user.role == 'SUPERVISOR':
        return redirect('supervisor_dashboard')
    elif request.user.role == 'CONDUCTOR':
        return redirect('driver_dashboard')
    elif request.user.role == 'CLIENTE':
        return redirect('client_dashboard')
    else:
        return redirect('login')


def admin_dashboard(request):
    return HttpResponse("Panel Administrador")


def supervisor_dashboard(request):
    return HttpResponse("Panel Supervisor")


def driver_dashboard(request):
    return HttpResponse("Panel Conductor")


def client_dashboard(request):
    return HttpResponse("Panel Cliente")