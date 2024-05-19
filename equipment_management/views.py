from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Equipment, Data, Alerts
from .serserializers import EquipmentSerializer,DataSerializer, AlertsSerializer


class IsInGroup(permissions.BasePermission):
    group_name = None
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.groups.filter(name=self.group_name).exists()
        return False

class IsAdminUser(IsInGroup):
    group_name = 'Admin'
class IsWorkerUser(IsInGroup):
    group_name = 'Worker'
class EquipmentListView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
class EquipmentInStorageListView(generics.ListAPIView):
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Equipment.objects.filter(status='in_storage')
class EquipmentUnderRepairListView(generics.ListAPIView):
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Equipment.objects.filter(status='under_repair')
class EquipmentWorkingListView(generics.ListAPIView):
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Equipment.objects.filter(status='working')

class EquipmentByResponsibleView(generics.ListAPIView):
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated , IsAdminUser]
    def get_queryset(self):
        responsible_id = self.kwargs['pk']
        return Equipment.objects.filter(responsible_id=responsible_id)
class EquipmentDataDetailView(generics.RetrieveUpdateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [permissions.IsAuthenticated]
class EquipmentAlertsDetailView(generics.RetrieveUpdateAPIView):
    queryset = Alerts.objects.all()
    serializer_class = AlertsSerializer
    permission_classes = [permissions.IsAuthenticated]
