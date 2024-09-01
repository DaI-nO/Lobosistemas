from rest_framework import viewsets
from .models import Vehiculo, Almacen
from .serializers import VehiculoSerializer, AlmacenSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class AlmacenViewSet(viewsets.ModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer
