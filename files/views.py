from rest_framework import viewsets
from .models import AttachedFile
from .serializers import AttachedFileSerializer


class AttachedFileViewSet(viewsets.ModelViewSet):
    queryset = AttachedFile.objects.all()
    serializer_class = AttachedFileSerializer
