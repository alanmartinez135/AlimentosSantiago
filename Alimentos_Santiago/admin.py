from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)

#agregaro desde rama proveedores
admin.site.register(Proveedor)
admin.site.register(PlatoProveedor)
admin.site.register(OfertaPlatoProveedor)