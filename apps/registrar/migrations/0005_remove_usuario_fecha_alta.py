# Generated by Django 3.1 on 2020-10-01 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0004_auto_20200930_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_alta',
        ),
    ]
