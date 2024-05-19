from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileSerializerforWorker(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'phone_number', 'first_name', 'last_name', 'address', 'position',]