from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete= models.CASCADE)
    run = models.IntegerField(verbose_name='run', unique=True)
    saldo = models.IntegerField(default=0)
    role = models.CharField(max_length=9, choices=settings.ROLES)
    def __str__(self):
        return f'{self.role}:  {self.user.username}'
    

class Empresa(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre de la empresa')
    run_empleado = models.ManyToManyField(UserProfile, related_name='empresa')
    # platos_disponibles = models.ManyToManyField(PlatoProveedor, related_name='plato_empresa')
    rut = models.CharField(max_length=12, unique=True) # rut de la empresa 
    direccion = models.CharField(max_length=50) # direccion de la empresa
    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField('Nombre proveedor', max_length=50, blank=False, null=False)
    pais = models.CharField('País', max_length=25, blank=False, null=False) # PAIS????
    fecha_contrato = models.DateField('Fecha de contrato', blank=False, null=False) # ????
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
    precio = models.IntegerField('Precio')
    stock = models.IntegerField()
    disponibilidad = models.BooleanField('Disponibilidad', default=True, blank=False, null=False) #mi no entender
    imagen = models.ImageField('Imagen del plato', upload_to='Alimentos_Santiago/media/platos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Plato Proveedor'
        verbose_name_plural = 'Platos Proveedores'
        ordering = ['proveedor', 'nombre_plato']

    def __str__(self):
        return f"{self.id} | Nombre plato : {self.nombre_plato} | Nombre proveedor : {self.proveedor.nombre} "
  
#Se alamcenana los datos despues de comprar en la tabla detalle compra     

class DetalleCompra(models.Model):
    producto = models.ForeignKey(PlatoProveedor, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_despacho = models.CharField(max_length=50)
    direccion_entrega = models.CharField(max_length=255, blank=True, null=True)  # Nuevo campo para la dirección de entrega
    fecha_compra = models.DateTimeField()
    usuario = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} || Producto: {self.producto.nombre_plato} || Cantidad: {self.cantidad}"
#agregaro desde rama proveedores


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
    
#CARRITO   
class Carrito(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Carrito de {self.usuario.username}'

class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    plato = models.ManyToManyField(PlatoProveedor)
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)  
    
    def __str__(self):
        return f'Detalle de {self.carrito.usuario.username}'
    
class RegistroEnvio(models.Model):
    
    estado_choices = [
        ('Pendiente', 'Pendiente'),
        ('En camino', 'En camino'),
        ('Entregado', 'Entregado'),
    ]
    
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    detalle = models.ForeignKey(DetalleCarrito, on_delete=models.CASCADE)
    repartidor = models.ForeignKey(Repartidores, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=estado_choices, default='Pendiente')
    
    def __str__(self):
        return f'Envio de {self.carrito.usuario.username}'