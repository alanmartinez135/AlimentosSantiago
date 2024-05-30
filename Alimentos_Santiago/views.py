from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def login(request):
    return render(request, 'login.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def perritos(request):
    return render(request, 'perritos.html')

def gatitos(request):
    return render(request, 'gatitos.html')

def contacto(request):
    return render(request, 'contacto.html')

def accesorios(request):
    return render(request, 'accesorios.html')

def alimentos(request):
    return render(request, 'alimentos.html')

def camas(request):
    return render(request, 'camas.html')

def identificador(request):
    return render(request, 'identificador.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def preguntasFrecuentes(request):
    return render(request, 'preguntasFrecuentes.html')

def suscripcion(request):
    return render(request, 'suscripcion.html')