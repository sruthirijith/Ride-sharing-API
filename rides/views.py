from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Ride
from .serializers import RideSerializer

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(rider=self.request.user)

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        ride = self.get_object()
        new_status = request.data.get('status')
        if new_status in dict(Ride.STATUS_CHOICES):
            ride.status = new_status
            ride.save()
            return Response({'status': ride.status})
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def match_driver(self, request, pk=None):
        ride = self.get_object()
        available_drivers = User.objects.filter(profile__is_driver=True, rides_as_driver__isnull=True)
        
        if available_drivers.exists():
            driver = available_drivers.first()
            ride.driver = driver
            ride.save()
            return Response({'driver': driver.username}, status=status.HTTP_200_OK)
        return Response({'error': 'No available drivers'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def update_location(self, request, pk=None):
        ride = self.get_object()
        new_location = request.data.get('current_location')
        if new_location:
            ride.current_location = new_location
            ride.save()
            return Response({'current_location': ride.current_location})
        return Response({'error': 'Current location not provided'}, status=status.HTTP_400_BAD_REQUEST)
