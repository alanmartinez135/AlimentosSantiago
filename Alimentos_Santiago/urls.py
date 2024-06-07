from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('registro', views.registro, name='registro'),
    path('inicio/', views.iniciosesion, name = "iniciosesion"),
    path('logout/', views.logout_view, name='logout'), #
    path('menu/', views.menu, name='menu'),
    path('chile/', views.chile, name='chile'),
    path('italia/', views.italia, name='italia'),
    path('china/', views.china, name='china'),
    path('peru/', views.peru, name='peru'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('preguntasFrecuentes/', views.preguntasFrecuentes, name='preguntasFrecuentes'),
]