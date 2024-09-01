from rest_framework import serializers
from .models import WorkOrder, OrdenTrabajo


class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'


class OrdenTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'
