from django.db import models


class CreateUpdateAbstract(models.Model):

    created_at = models.DateField('дата создания', auto_now_add=True)
    updated_at = models.DateField('дата обновления', auto_now=True)

    class Meta:
        abstract = True


class Company(CreateUpdateAbstract):

    company_token = models.TextField('токен')

    class Meta:
        ordering = ('-updated_at', '-created_at', 'id')
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.company_token
