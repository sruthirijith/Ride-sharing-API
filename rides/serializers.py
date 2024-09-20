from rest_framework import serializers
from .models import Ride

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'rider', 'driver', 'pickup_location', 'dropoff_location', 'current_location','status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'rider', 'driver', 'created_at', 'updated_at']

    def validate_status(self, value):
        """Custom validation for status field."""
        if value not in dict(Ride.STATUS_CHOICES):
            raise serializers.ValidationError("Invalid status.")
        return value

    def validate_location(self, value):
        """Custom validation for location field."""
        if not isinstance(value, str):
            raise serializers.ValidationError("Invalid location format.")
        return value