# Generated by Django 2.2.3 on 2020-11-27 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0002_auto_20201127_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deporte',
            name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='deporte',
            name='created',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de publicacion'),
        ),
        migrations.AddField(
            model_name='deporte',
            name='modified',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de modificacion'),
        ),
    ]
