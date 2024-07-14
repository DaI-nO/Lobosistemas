from rest_framework import viewsets
from .models import AdditionalCost, TotalCost
from .serializers import AdditionalCostSerializer, TotalCostSerializer


class AdditionalCostViewSet(viewsets.ModelViewSet):
    queryset = AdditionalCost.objects.all()
    serializer_class = AdditionalCostSerializer


class TotalCostViewSet(viewsets.ModelViewSet):
    queryset = TotalCost.objects.all()
    serializer_class = TotalCostSerializer
