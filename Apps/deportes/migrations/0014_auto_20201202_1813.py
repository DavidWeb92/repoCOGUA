# Generated by Django 2.2.3 on 2020-12-02 23:13

from django.db import migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0013_deporte_imagen_prueba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deporte',
            name='imagen_prueba',
        ),
        migrations.AlterField(
            model_name='deporte',
            name='imagen',
            field=smartfields.fields.ImageField(blank=True, max_length=200, null=True, upload_to='imagenes/deportes/%Y/%m/%d/', verbose_name='Imagen'),
        ),
    ]
