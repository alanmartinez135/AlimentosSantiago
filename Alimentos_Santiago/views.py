from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from Alimentos_Santiago.Carrito import Carrito

# Create your views here.

def inicio(request):
    # Para que se muestren los platos que la empresa requeria de platos
#    user = request.user
    perfil = request.session.get('perfil')
#     if user.is_authenticated:
#         try:
#             user_profile = UserProfile.objects.get(user=user)
#             empresa = user_profile.empresa.first()  # Obtener la primera empresa asociada al perfil
#         except UserProfile.DoesNotExist:
#             user_profile = None
#             empresa = None

#         if empresa:
#             platos = empresa.platos_disponibles.filter(disponibilidad=True)
#         else:
#             platos = PlatoProveedor.objects.filter(disponibilidad=True)
#     else:
#         platos = PlatoProveedor.objects.filter(disponibilidad=True)

    platos = PlatoProveedor.objects.filter(stock__gt=0)

    context = {
        'perfil': perfil,
        'platos': platos,
    }

    return render(request, 'public/inicio.html', context)

def registro(request):
    if request.method == 'POST':
        us = request.POST.get('InputUsuario')
        correo = request.POST.get('InputEmail1')
        run = request.POST.get('run')
        contrasenia = request.POST.get('InputPassword1')
        role = 'cliente'

        if User.objects.filter(username=us).exists():
            messages.error(request, 'El usuario ya está en uso')
            return render(request, 'auth/registro.html')

        if User.objects.filter(email=correo).exists():
            messages.error(request, 'El correo ya está en uso')
            return render(request, 'auth/registro.html')

        if User.objects.filter(id=run).exists():
            messages.error(request, 'El rut ya está en uso')
            return render(request, 'auth/registro.html')

        # Verifica que 'us' no esté vacío o nulo antes de crear el usuario
        if not us:
            messages.error(request, 'El nombre de usuario es obligatorio')
            return render(request, 'auth/registro.html')

        user = User.objects.create_user(username=us, email=correo, password=contrasenia)

        UserProfile.objects.create(user=user, run=run, role=role)
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

def detalle_plato(request, id):
    perfil = request.session.get('perfil')
    plato = get_object_or_404(PlatoProveedor, id=id)

    context = {
        'perfil': perfil,
        'plato': plato,
    }
    return render(request, 'public/detalle_plato.html', context)

# def carrito(request):
#     return render(request, 'public/carrito.html')

def carro(request):
    productos = PlatoProveedor.objects.all()
    return render(request, "public/carrito.html", {"productos":productos})

def descrip_carro(request):
    return render(request, 'public/descrip_carrito.html')

def lista_productos(request):
    productos = PlatoProveedor.objects.all()  # Obtén todos los productos (ajusta la consulta según tu modelo)
    context = {
        'productos': productos,
    }
    return render(request, "carrito", context)

def agregar_producto(request, producto_id):
    v_carrito = Carrito(request)
    producto = PlatoProveedor.objects.get(id=producto_id)
    v_carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    v_carrito = Carrito(request)
    producto = PlatoProveedor.objects.get(id=producto_id)
    v_carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    v_carrito = Carrito(request)
    producto = PlatoProveedor.objects.get(id=producto_id)
    v_carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    v_carrito = Carrito(request)
    v_carrito.limpiar()
    return redirect("carrito")

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