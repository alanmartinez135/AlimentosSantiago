from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'public/inicio.html')

def login(request):
    return render(request, 'login.html')

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

def sesion(request):
    return render(request, 'auth/ini_sesion.html')
