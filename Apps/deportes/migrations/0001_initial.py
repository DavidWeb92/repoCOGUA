# Generated by Django 2.2.3 on 2020-11-16 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=200, verbose_name='Precio')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('estado', models.BooleanField(default=False, verbose_name='No Reservado/Reservado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Deporte',
                'verbose_name_plural': 'Deportes',
                'ordering': ['nombre'],
            },
        ),
    ]
