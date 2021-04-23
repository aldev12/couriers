from rest_framework import serializers

from devices.models import Location, Device


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['latitude', 'longitude', 'company', 'device', 'data', 'updated_at', 'created_at']


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ['company', 'device', 'device_model', 'app', 'version', 'updated_at', 'created_at']


class DeviceLastLocationSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    class Meta:
        model = Device
        fields = ['device_model', 'latitude', 'longitude']

    def get_latitude(self, obj):
        return obj['location__latitude']

    def get_longitude(self, obj):
        return obj['location__longitude']
