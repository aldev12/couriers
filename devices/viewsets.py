from rest_framework import viewsets, permissions

from devices.models import Location, Device
from devices.serializers import LocationSerializer, DeviceLastLocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceLastLocationViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Device.last_location_objects.all()
    serializer_class = DeviceLastLocationSerializer
    permission_classes = [permissions.IsAuthenticated]
