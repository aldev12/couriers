from django.contrib import admin

from devices.models import Device, Location


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('updated_at', 'created_at','company', 'device', 'device_model', 'app', 'version', )
    readonly_fields = ('updated_at', 'created_at', )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    change_list_template = "admin/devices/location_changelist.html"

    list_display = ('updated_at', 'created_at', 'latitude', 'longitude', 'company', 'device', 'data', )
    readonly_fields = ('updated_at', 'created_at', )
    search_fields = ('devices', )
