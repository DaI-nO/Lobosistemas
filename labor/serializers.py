from rest_framework import serializers
from .models import LaborDetail


class LaborDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaborDetail
        fields = '__all__'
