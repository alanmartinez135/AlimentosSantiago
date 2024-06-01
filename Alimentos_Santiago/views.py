from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

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

