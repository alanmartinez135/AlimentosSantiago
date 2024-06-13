# Generated by Django 5.0.6 on 2024-06-13 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alimentos_Santiago', '0006_rename_tipo_despacho_detallepedido_retiro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallepedido',
            name='retiro',
            field=models.CharField(choices=[('TIENDA', 'En tienda'), ('DELIVERY', 'Delivery')], default='TIENDA', max_length=10, verbose_name='Tipo de retiro'),
        ),
    ]