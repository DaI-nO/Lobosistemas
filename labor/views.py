from rest_framework import viewsets
from .models import LaborDetail
from .serializers import LaborDetailSerializer


class LaborDetailViewSet(viewsets.ModelViewSet):
    queryset = LaborDetail.objects.all()
    serializer_class = LaborDetailSerializer
