# Generated by Django 3.1 on 2020-09-28 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id_localidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_provincia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Transportista',
            fields=[
                ('id_transportista', models.AutoField(primary_key=True, serialize=False)),
                ('cedula_azul', models.CharField(max_length=200)),
                ('cedula_verde', models.CharField(max_length=200)),
                ('fecha_alta', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Transportista',
                'verbose_name_plural': 'Transportistas',
                'ordering': ['id_transportista'],
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id_vehiculo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=200)),
                ('venc_tecnica', models.DateField()),
                ('patente', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('capacidad', models.CharField(max_length=200)),
                ('fecha_alta', models.DateField(auto_now=True)),
                ('transp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrar.transportista')),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=50)),
                ('cuil_cuit', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_alta', models.DateField(auto_now=True)),
                ('localidad', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registrar.localidad')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['id_usuario'],
            },
        ),
        migrations.AddField(
            model_name='transportista',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registrar.usuario'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='id_provincia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registrar.provincia'),
        ),
    ]
