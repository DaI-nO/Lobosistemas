from rest_framework import serializers
from .models import PartMaterial


class PartMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartMaterial
        fields = '__all__'
