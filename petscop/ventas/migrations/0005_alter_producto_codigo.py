# Generated by Django 4.2.2 on 2023-06-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_egreso_productosegreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]