from django.db import models

# Create your models here.


class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, blank=False)
    nombre = models.CharField(max_length=40, blank=False)
    apellido_paterno = models.CharField(max_length=20, blank=False )
    telefono = models.CharField(max_length=9)
    email = models.EmailField(
        unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField()
    contraseña = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'clientes'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nombre


class Producto (models.Model):
    codigo = models.CharField(
        max_length=255, unique=True, null=True, blank=True)
    descripcion = models.CharField(max_length=255, unique=True, null=False)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    costo = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2, null=False)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        order_with_respect_to = 'descripcion'

    def __str__(self):
        return self.descripcion

