# Generated by Django 5.0.6 on 2024-06-12 23:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alimentos_Santiago', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repartidores',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Repartidor')),
                ('fecha_contrato', models.DateField(verbose_name='Fecha de contrato')),
                ('telefono', models.CharField(max_length=30, verbose_name='Teléfono')),
                ('correo', models.EmailField(max_length=50, verbose_name='Correo')),
                ('disponibilidad', models.BooleanField(default=True, verbose_name='Disponibilidad')),
            ],
            options={
                'verbose_name': 'Repartidor',
                'verbose_name_plural': 'Repartidores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='DestinoRepartidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_despacho', models.DateField(verbose_name='Fecha Despacho')),
                ('hora_despacho', models.TimeField(default='00:00:00', verbose_name='Hora Despacho')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('repartidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alimentos_Santiago.repartidores')),
            ],
            options={
                'verbose_name': 'Destino Repartidor',
                'verbose_name_plural': 'Destinos Repartidores',
                'ordering': ['fecha_despacho'],
            },
        ),
    ]