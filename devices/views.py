from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from couriers.settings import GOOGLE_MAPS_KEY
from devices.models import Device


class DevicesLocation(LoginRequiredMixin, TemplateView):
    template_name = 'admin/devices/devices_location.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data()

        objects = Device.last_location_objects.all()

        kwargs['objects'] = objects
        if GOOGLE_MAPS_KEY:
            kwargs['google_maps_key'] = GOOGLE_MAPS_KEY
        else:
            messages.add_message(self.request, messages.ERROR, 'Задайте ключ GOOGLE MAPS  в настройках')

        return kwargs


