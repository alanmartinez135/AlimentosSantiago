# Generated by Django 5.0.6 on 2024-06-12 23:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alimentos_Santiago', '0002_repartidores_destinorepartidor'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinorepartidor',
            name='plato',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Alimentos_Santiago.platoproveedor'),
            preserve_default=False,
        ),
    ]
