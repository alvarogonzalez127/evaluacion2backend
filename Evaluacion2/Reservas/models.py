from django.db import models

# Create your models here.

class reserva(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fechareserva = models.DateField()
    horareserva = models.TimeField()
    cantidadpersonas = models.IntegerField()
    estado = models.CharField(max_length=25)
    observacion = models.CharField(max_length=255)