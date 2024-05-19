from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer, ProfileSerializerforWorker


# Create your views here.
class WorkerListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Admin').exists():
            return Profile.objects.all()
        else:
            return Profile.objects.all()
class WorkerCreateView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Admin').exists():
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        return super().post(request, *args, **kwargs)


class WorkerDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializerforWorker
    permission_classes = [permissions.IsAuthenticated]