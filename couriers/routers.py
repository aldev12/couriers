from rest_framework import routers

from devices.viewsets import LocationViewSet, DeviceLastLocationViewSet

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'devices_last_location', DeviceLastLocationViewSet)