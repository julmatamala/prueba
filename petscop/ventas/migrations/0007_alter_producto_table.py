# Generated by Django 4.2.2 on 2023-06-28 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_alter_producto_codigo'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='producto',
            table='ventas_producto',
        ),
    ]
