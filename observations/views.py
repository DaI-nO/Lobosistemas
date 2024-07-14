from rest_framework import viewsets
from .models import Observation
from .serializers import ObservationSerializer


class ObservationViewSet(viewsets.ModelViewSet):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer
