# Generated by Django 2.2.3 on 2020-12-17 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_final',
            field=models.DateField(verbose_name='Fecha final de reserva'),
        ),
    ]