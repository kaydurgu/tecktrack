from django.urls import path, include
from .views import (EquipmentListView, EquipmentDetailView, EquipmentInStorageListView, EquipmentUnderRepairListView
, EquipmentWorkingListView, EquipmentByResponsibleView, EquipmentDataDetailView, EquipmentAlertsDetailView, EquipmentAlertsCriticalDetailView,
  EquipmentAlertsHighDetailView, EquipmentAlertsMediumDetailView,EquipmentAlertsLowDetailView)

urlpatterns = [
    path('list/', EquipmentListView.as_view(), name='list-equipment'),
    path('list/instorage', EquipmentInStorageListView.as_view(), name='list-equipment-inStorage'),
    path('list/underrepair', EquipmentUnderRepairListView.as_view(), name='list-equipment-underRepair'),

    path('list/working', EquipmentWorkingListView.as_view(), name='list-equipment-working'),
    path('<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('data/<int:pk>/', EquipmentDataDetailView.as_view(), name='equipment-data-detail'),
    path('alerts/<int:pk>/', EquipmentAlertsDetailView.as_view(), name='equipment-alerts-detail'),

    path('alerts/critical/', EquipmentAlertsCriticalDetailView.as_view(), name='equipment-alerts-critical'),
    path('alerts/high/', EquipmentAlertsHighDetailView.as_view(), name='equipment-alerts-high'),
    path('alerts/medium/', EquipmentAlertsMediumDetailView.as_view(), name='equipment-alerts-medium'),
    path('alerts/low/', EquipmentAlertsLowDetailView.as_view(), name='equipment-alerts-low'),

    path('responsible/<int:pk>/', EquipmentByResponsibleView.as_view(), name='equipment-by-responsible'),

]
