from rest_framework import serializers
from .models import Vehiculo, Almacen

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = '__all__'
