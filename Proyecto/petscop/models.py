import datetime
from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    cantidad= models.IntegerField(null=True)
    descripcion= models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    tipo_producto = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="productos", null=True, )

    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateField(blank=False, null=False, default = datetime.datetime.now)

    def __str__(self):
        return str(self.id_boleta)    

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta) 
