# Generated by Django 3.1 on 2020-10-01 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0006_auto_20200930_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fecha_alta',
            field=models.DateField(auto_now=True),
        ),
    ]
