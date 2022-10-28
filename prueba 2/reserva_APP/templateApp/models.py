from django.db import models

# Create your models here.
class reservas(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.CharField(max_length=10)
    cantidadPersonas = models.IntegerField()
    estado = models.CharField(max_length=20)
    observacion = models.CharField(max_length=50)
