from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete= models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES)
    def __str__(self):
        return f'{self.user.username} - {self.role}'
    


#agregaro desde rama proveedores
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre proveedor', max_length=50, blank=False, null=False)
    pais = models.CharField('País', max_length=25, blank=False, null=False)
    fecha_contrato = models.DateField('Fecha de contrato', blank=False, null=False)
    telefono = models.CharField('Teléfono', max_length=30, blank=False, null=False)
    correo = models.EmailField('Correo', max_length=50, blank=False, null=False)
    especialidad_tipo_plato = models.CharField('Especialidad tipo de plato', max_length=25, blank=False, null=False)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']

    def __str__(self):
        return f"{self.id} | Nombre del proveedor : {self.nombre} | Especialidad : {self.especialidad_tipo_plato}"

class PlatoProveedor(models.Model):
    id = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre_plato = models.CharField('Nombre del plato', max_length=100, blank=False, null=False)
    descripcion = models.TextField()
    precio = models.DecimalField('Precio', max_digits=10, decimal_places=2, blank=False, null=False)
    disponibilidad = models.BooleanField('Disponibilidad', default=True, blank=False, null=False)
    imagen = models.ImageField('Imagen del plato', upload_to='Alimentos_Santiago/media/platos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Plato Proveedor'
        verbose_name_plural = 'Platos Proveedores'
        ordering = ['proveedor', 'nombre_plato']

    def __str__(self):
        return f"{self.id} | Nombre plato : {self.nombre_plato} | Nombre proveedor : {self.proveedor.nombre} "

    
#------------------------------------------------------------------------------------------------------------------------

    #REPARTIDOR
class Repartidores(models.Model):
    rut = models.CharField('Rut',max_length=10, primary_key=True)
    nombre = models.CharField('Nombre Repartidor', max_length=50, blank=False, null=False)
    fecha_contrato = models.DateField('Fecha de contrato', blank=False, null=False)
    telefono = models.CharField('Teléfono', max_length=30, blank=False, null=False)
    correo = models.EmailField('Correo', max_length=50, blank=False, null=False)
    disponibilidad = models.BooleanField('Disponibilidad', default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Repartidor'
        verbose_name_plural = 'Repartidores'
        ordering = ['nombre']

    def __str__(self):
        return f"Rut Repartidor : {self.rut} | Nombre del Repartidor : {self.nombre} | Disponibilidad : {self.disponibilidad}"

    #DESTINO
class DestinoRepartidor(models.Model):
    repartidor = models.ForeignKey(Repartidores, on_delete=models.CASCADE)
    fecha_despacho = models.DateField('Fecha Despacho', blank=False, null=False)
    hora_despacho = models.TimeField('Hora Despacho', default='00:00:00', blank=False, null=False)
    direccion = models.CharField('Direccion', max_length=100, blank=False, null=False)
    
    class Meta:
        verbose_name = 'Destino Repartidor'
        verbose_name_plural = 'Destinos Repartidores'
        ordering = ['fecha_despacho']

    def __str__(self):
        return f"{self.repartidor} | Fecha Despacho : {self.fecha_despacho} | Direccion : {self.direccion}"
