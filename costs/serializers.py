from rest_framework import serializers
from .models import AdditionalCost, TotalCost


class AdditionalCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalCost
        fields = '__all__'


class TotalCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalCost
        fields = '__all__'
