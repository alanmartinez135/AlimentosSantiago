from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import role_required

# Create your views here.

def inicio(request):
    perfil = request.session.get('perfil')
    context = {
        'perfil': perfil,
    } 
    return render(request, 'public/inicio.html', context)

def registro(request):
    if request.method == 'POST': 
        us = request.POST.get('InputUsuario')
        correo = request.POST.get('InputEmail1')
        contrasenia = request.POST.get('InputPassword1')
        role = 'cliente'

        if User.objects.filter(username=us).exists():
            messages.error(request, 'El usuario ya está en uso')
            return render(request, 'auth/registro.html')
        
        if User.objects.filter(email=correo).exists():
            messages.error(request, 'El correo ya está en uso')
            return render(request, 'auth/registro.html')

        # Verifica que 'us' no esté vacío o nulo antes de crear el usuario
        if not us:
            messages.error(request, 'El nombre de usuario es obligatorio')
            return render(request, 'auth/registro.html')

        user = User.objects.create_user(username=us, email=correo, password=contrasenia)
        
        UserProfile.objects.create(user=user, role=role)
        return redirect('inicio')
        # Resto de tu lógica aquí (redireccionar, etc.)

    return render(request, 'auth/registro.html')

def iniciosesion(request):
    error_message = None  # Variable para almacenar el mensaje de error
    if request.method == 'POST':
        usuario = request.POST['InputUsuario']  # Se obtiene el usuario
        contrasenia = request.POST['InputPassword1']  # Se obtiene la contraseña
        user = authenticate(request, username=usuario, password=contrasenia)  # Autenticar usuario
        if user is not None:
            profile = UserProfile.objects.get(user=user)  # Obtener el perfil del usuario
            request.session['perfil'] = profile.role  # Guardar el rol en la sesión
            auth_login(request, user)  # Iniciar sesión
            return redirect('inicio')  # Redirigir a la página de inicio
        else:
            error_message = 'Usuario o contraseña incorrectos, intente de nuevo.'  # Mensaje de error
    return render(request, 'auth/iniciosesion.html', {'error_message': error_message})  # Renderizar la página con mensaje de error

@login_required
@role_required('admin', 'cliente')
def logout_view(request):
    auth_logout(request)
    return redirect('inicio')

def menu(request):
    return render(request, 'menu.html')

def chile(request):
    return render(request, 'chile.html')

def italia(request):
    return render(request, 'italia.html')

def china(request):
    return render(request, 'china.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def peru(request):
    return render(request, 'peru.html')

def preguntasFrecuentes(request):
    return render(request, 'preguntasFrecuentes.html')