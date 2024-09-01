from django.db import models

class Vehiculo(models.Model):
    numero_de_vehiculo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    ano = models.IntegerField()
    numero_chasis = models.CharField(max_length=100, blank=True)
    categoria = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=100, blank=True)
    numero_vin = models.CharField(max_length=50, blank=True)
    placas = models.CharField(max_length=50, blank=True)
    modelo = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=50)
    objetivo_utilizacion = models.TextField(blank=True)
    estado_registro = models.CharField(max_length=100, blank=True)
    fecha_exp_registro = models.DateField(null=True, blank=True)
    nombre_operador = models.CharField(max_length=100, blank=True)
    prioridad_mantenimiento = models.CharField(max_length=50)
    notas = models.TextField(blank=True)
    ubicacion_geografica = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre

class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
