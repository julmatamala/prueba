# Generated by Django 4.2.3 on 2023-07-12 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petscop', '0003_boleta_alter_producto_precio_detalle_boleta'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
    ]