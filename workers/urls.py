from django.urls import path, include
from .views import WorkerListView, WorkerCreateView, WorkerDetailView

urlpatterns = [
    path('', WorkerListView.as_view(), name='workers-list'),
    path('auth/', include('rest_framework.urls')),
    path('<int:pk>/', WorkerDetailView.as_view(), name='worker-detail'),
    path('create/', WorkerCreateView.as_view(), name='worker-create'),
]
