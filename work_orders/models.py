from django.db import models


class WorkOrder(models.Model):
    title = models.CharField(max_length=255)
    memorandum = models.TextField()
    priority = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=255)
    work_order_type = models.CharField(max_length=50)
    link_inspection = models.TextField()
    link_work_order = models.TextField()
    vehicle_number = models.CharField(max_length=50)
    vehicle_name = models.CharField(max_length=255)
    vehicle_model = models.CharField(max_length=255)
    meter_reading = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    estimated_time = models.DecimalField(max_digits=10, decimal_places=2)

class OrdenTrabajo(models.Model):
    PRIORIDAD_CHOICES = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    ]

    titulo = models.CharField(max_length=200)
    memorandum = models.TextField(blank=True, null=True)
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES)
    asignado_a = models.CharField(max_length=100, blank=True, null=True)
    tipo_orden_trabajo = models.CharField(max_length=100, blank=True, null=True)
    inspeccion_enlaces = models.CharField(max_length=100, blank=True, null=True)
    orden_trabajo_enlace = models.CharField(max_length=100, blank=True, null=True)
    numero_vehiculo = models.CharField(max_length=50)
    nombre_vehiculo = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    lectura_medidor = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tiempo_trabajo_estimado = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.titulo