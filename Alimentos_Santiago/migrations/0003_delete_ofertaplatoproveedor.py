# Generated by Django 5.0.6 on 2024-06-12 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alimentos_Santiago', '0002_proveedor_platoproveedor_ofertaplatoproveedor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OfertaPlatoProveedor',
        ),
    ]