from rest_framework import serializers
from .models import Equipment, Data, Alerts

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
        read_only_fields = ['equipment']
class AlertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerts
        fields = '__all__'
        read_only_fields = ['equipment']
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
        read_only_fields = ['added_by']
    data = DataSerializer(many=True, read_only=True)
    alerts = AlertsSerializer(many=True, read_only=True)
