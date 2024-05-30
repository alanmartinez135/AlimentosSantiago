"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Alimentos_Santiago.views import login, registrarse, perritos, gatitos, contacto, accesorios, alimentos, camas, identificador, nosotros, preguntasFrecuentes, suscripcion

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Alimentos_Santiago.urls")),
    path('login/', login, name='login'),
    path('registrarse/', registrarse, name='registrarse'),
    path('perritos/', perritos, name='perritos'),
    path('gatitos/', gatitos, name='gatitos'),
    path('contacto/', contacto, name='contacto'),
    path('accesorios/', accesorios, name='accesorios'),
    path('alimentos/', alimentos, name='alimentos'),
    path('camas/', camas, name='camas'),
    path('identificador/', identificador, name='identificador'),
    path('nosotros/', nosotros, name='nosotros'),
    path('preguntasFrecuentes/', preguntasFrecuentes, name='preguntasFrecuentes'),
    path('suscripcion/', suscripcion, name='suscripcion'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)