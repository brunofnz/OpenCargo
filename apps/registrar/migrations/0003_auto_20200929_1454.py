# Generated by Django 3.1 on 2020-09-29 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0002_auto_20200928_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
    ]
