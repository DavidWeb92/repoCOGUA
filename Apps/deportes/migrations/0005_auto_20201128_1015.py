# Generated by Django 2.2.3 on 2020-11-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0004_auto_20201128_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deporte',
            name='imagen',
        ),
        migrations.AddField(
            model_name='deporte',
            name='imagen_deporte',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='deporte/', verbose_name='Imagen'),
        ),
    ]