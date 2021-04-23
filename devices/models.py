from django.db import models
from django.db.models import F, Max

from companies.models import Company, CreateUpdateAbstract


class LastLocationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            last_location=Max('location__id', latitude='location__latitude', longitude='location__longitude')
        ).filter(
            location__id=F('last_location')
        ).values('location__latitude', 'location__longitude', 'device_model')


class Device(CreateUpdateAbstract):

    company = models.ForeignKey(Company, verbose_name='организация', on_delete=models.CASCADE)
    device = models.TextField('идентификатор устройства')
    device_model = models.TextField('моедль устройства')
    app = models.TextField('приложение')
    version = models.TextField('версия')

    objects = models.Manager()
    last_location_objects = LastLocationManager()

    class Meta:
        ordering = ('-updated_at', '-created_at', 'id')
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

    def __str__(self):
        return f'{self.device} {self.device_model}'


class Location(CreateUpdateAbstract):

    latitude = models.DecimalField('широта', max_digits=9, decimal_places=6)
    longitude = models.DecimalField('долгота', max_digits=9, decimal_places=6)
    company = models.ForeignKey(Company, verbose_name='организация', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, verbose_name='устройство', on_delete=models.CASCADE)
    data = models.JSONField('данные с устройства')

    class Meta:
        ordering = ('-updated_at', '-created_at', 'id')
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'
