from rest_framework import serializers
from .models import AttachedFile


class AttachedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = '__all__'
