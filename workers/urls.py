from django.urls import path, include
from .views import WorkerListView, WorkerCreateView, WorkerDetailView

urlpatterns = [
    path('', WorkerListView.as_view(), name='WorkersList'),
    path('<int:pk>/', WorkerDetailView.as_view(), name='WorkerCreate'),
    path('create/', WorkerCreateView.as_view(), name='WorkerCreate'),
]
