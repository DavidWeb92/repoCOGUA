# Generated by Django 2.2.3 on 2020-11-28 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0007_auto_20201128_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deporte',
            old_name='imagen_deporte',
            new_name='imagen',
        ),
    ]