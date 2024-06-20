from django.contrib import admin
from .models import *

# necesito hacer filtros para las empresas
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'rut', 'direccion', 'get_empleados') # busca nombre de la empresa, rut, direccion y empleados
    search_fields = ('nombre', 'rut', 'direccion') # busca por nombre, rut y direccion
    list_filter = ('nombre', 'rut', 'direccion') # filtra por nombre, rut y direccion
    
    def get_empleados(self, obj): # ontentos los empleados de la empresa
        return ", ".join([empleado.user.username for empleado in obj.run_empleado.all()]) # retorna los empleados de la empresa  --inner join
    get_empleados.short_description = 'Empleados'
    
# Register your models here.
admin.site.register(UserProfile)

#agregaro desde rama proveedores
admin.site.register(Proveedor)
admin.site.register(PlatoProveedor)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Repartidores)
admin.site.register(DetalleCompra)

