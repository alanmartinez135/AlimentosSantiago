# Create your models here.
from django.db import models

class Categoria(models.Model): # clase que representa una tabla en la base de datos
    nombre = models.CharField(max_length=100) # campo de texto con un máximo de 100 caracteres
    descripcion = models.TextField() # campo de texto largo
    fecha_creacion = models.DateTimeField(auto_now_add=True) # campo de fecha y hora con valor predeterminado de la fecha y hora actual

    def str(self): # método para representar el objeto como una cadena
        return self.nombre # devuelve el nombre de la categoría

class Producto(models.Model): # clase que representa una tabla en la base de datos
    nombre = models.CharField(max_length=100) # campo de texto con un máximo de 100 caracteres
    descripcion = models.TextField() # campo de texto largo
    precio = models.DecimalField(max_digits=10, decimal_places=2) # campo de número decimal con un máximo de 10 dígitos y 2 decimales
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) # campo de clave foránea que hace referencia a la tabla de categoria y se elimina en cascada
    fecha_creacion = models.DateTimeField(auto_now_add=True) # campo de fecha y hora con valor predeterminado de la fecha y hora actual

    def str(self): # método para representar el objeto como una cadena
        return self.nombre, self.precio # devuelve el nombre y precio del producto

class Usuario(models.Model):
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20) 
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)

def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   
