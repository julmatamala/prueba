# Generated by Django 4.2.2 on 2023-06-26 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_cliente_id_alter_cliente_rut_alter_producto_cantidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]