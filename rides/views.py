from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Ride
from .serializers import RideSerializer

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(rider=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        """Handles partial updates, including status and current location."""
        ride = self.get_object()
        serializer = self.get_serializer(ride, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

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
