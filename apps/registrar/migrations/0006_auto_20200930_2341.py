# Generated by Django 3.1 on 2020-10-01 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0005_remove_usuario_fecha_alta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrar.localidad'),
        ),
    ]
