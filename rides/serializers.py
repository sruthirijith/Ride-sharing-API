from rest_framework import serializers
from .models import Ride

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'rider', 'driver', 'pickup_location', 'dropoff_location', 'current_location','status', 'created_at', 'updated_at']
        read_only_fields = ['rider', 'created_at', 'updated_at', 'status']
