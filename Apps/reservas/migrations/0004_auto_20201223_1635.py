# Generated by Django 2.2.3 on 2020-12-23 21:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deportes', '0014_auto_20201202_1813'),
        ('reservas', '0003_auto_20201223_1631'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReservaDeporte',
            new_name='Reserva_Deporte',
        ),
    ]
