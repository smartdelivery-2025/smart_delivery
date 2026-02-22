from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirección por rol
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'supervisor':
                return redirect('supervisor_dashboard')
            elif user.role == 'driver':
                return redirect('driver_dashboard')

        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})

    return render(request, 'login.html')


def register_view(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'register.html', {'form': form})
