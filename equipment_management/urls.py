from django.urls import path, include
from .views import EquipmentListView


urlpatterns = [
    path('list/', EquipmentListView.as_view(), name='list-equipment'),
]