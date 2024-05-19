from django.urls import path, include
from .views import (EquipmentListView, EquipmentDetailView, EquipmentInStorageListView, EquipmentUnderRepairListView
    , EquipmentWorkingListView, EquipmentByResponsibleView, EquipmentDataDetailView)


urlpatterns = [
    path('list/', EquipmentListView.as_view(), name='list-equipment'),
    path('list/instorage', EquipmentInStorageListView.as_view(), name='list-equipment-inStorage'),
    path('list/underrepair', EquipmentUnderRepairListView.as_view(), name='list-equipment-underRepair'),
    path('list/working', EquipmentWorkingListView.as_view(), name='list-equipment-working'),
    path('<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('data/<int:pk>/', EquipmentDataDetailView.as_view(), name='equipment-data-detail'),
    path('responsible/<int:pk>/', EquipmentByResponsibleView.as_view(), name='equipment-by-responsible'),

]