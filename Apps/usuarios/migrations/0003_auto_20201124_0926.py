# Generated by Django 2.2.3 on 2020-11-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20201124_0856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario_administrador',
            new_name='is_staff',
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
