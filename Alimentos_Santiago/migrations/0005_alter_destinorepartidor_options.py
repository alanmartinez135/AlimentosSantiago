# Generated by Django 5.0.6 on 2024-06-09 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alimentos_Santiago', '0004_rename_destino_destinorepartidor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destinorepartidor',
            options={'ordering': ['fecha_despacho'], 'verbose_name': 'Destino Repartidor', 'verbose_name_plural': 'Destinos Repartidores'},
        ),
    ]
