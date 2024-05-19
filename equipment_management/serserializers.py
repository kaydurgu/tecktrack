from rest_framework import serializers
from .models import Equipment, Data, Alerts

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class AlertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerts
        fields = '__all__'