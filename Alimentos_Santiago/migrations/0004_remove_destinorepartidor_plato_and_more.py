# Generated by Django 5.0.6 on 2024-06-12 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alimentos_Santiago', '0003_destinorepartidor_plato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinorepartidor',
            name='plato',
        ),
        migrations.AddField(
            model_name='destinorepartidor',
            name='plato',
            field=models.ManyToManyField(to='Alimentos_Santiago.platoproveedor'),
        ),
    ]