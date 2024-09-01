from rest_framework import viewsets
from .models import WorkOrder, OrdenTrabajo
from .serializers import WorkOrderSerializer, OrdenTrabajoSerializer


class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer



class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
