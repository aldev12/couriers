# Generated by Django 3.2 on 2021-04-21 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='дата обновления')),
                ('device', models.TextField(verbose_name='идентификатор устройства')),
                ('device_model', models.TextField(verbose_name='моедль устройства')),
                ('app', models.TextField(verbose_name='приложение')),
                ('version', models.TextField(verbose_name='версия')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='организация')),
            ],
            options={
                'verbose_name': 'Устройство',
                'verbose_name_plural': 'Устройства',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='дата обновления')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='широта')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='долгота')),
                ('data', models.JSONField(verbose_name='данные с устройства')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='организация')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device', verbose_name='устройство')),
            ],
            options={
                'verbose_name': 'Местоположение',
                'verbose_name_plural': 'Местоположения',
            },
        ),
    ]
