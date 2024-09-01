from django.contrib import admin
from .models import WorkOrder, OrdenTrabajo

admin.site.register(WorkOrder)



@admin.register(OrdenTrabajo)
class OrdenTrabajoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'numero_vehiculo', 'nombre_vehiculo', 'prioridad', 'fecha_inicio', 'fecha_vencimiento')
    search_fields = ('titulo', 'numero_vehiculo', 'nombre_vehiculo')
    list_filter = ('prioridad', 'fecha_inicio', 'fecha_vencimiento')
