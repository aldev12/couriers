from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from couriers.routers import router
from devices.views import DevicesLocation

urlpatterns = [
    url('^admin/map_locations/', DevicesLocation.as_view(), name='devices-location'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
