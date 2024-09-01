from django.contrib import admin
from .models import Vehiculo, Almacen

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero_de_vehiculo', 'modelo', 'fabricante', 'estado']
    search_fields = ['nombre', 'numero_de_vehiculo', 'modelo']

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion']
    search_fields = ['nombre']
