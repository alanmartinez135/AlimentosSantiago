# Generated by Django 5.0.6 on 2024-06-20 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alimentos_Santiago', '0003_remove_detallecompra_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Alimentos_Santiago.userprofile'),
            preserve_default=False,
        ),
    ]