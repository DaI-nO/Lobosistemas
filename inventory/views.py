from rest_framework import viewsets
from .models import PartMaterial
from .serializers import PartMaterialSerializer


class PartMaterialViewSet(viewsets.ModelViewSet):
    queryset = PartMaterial.objects.all()
    serializer_class = PartMaterialSerializer
