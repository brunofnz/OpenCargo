# Generated by Django 3.1 on 2020-09-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrarCliente', '0003_transportista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.RemoveField(
            model_name='transportista',
            name='id',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transportista',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
