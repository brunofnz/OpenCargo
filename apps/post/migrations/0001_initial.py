# Generated by Django 3.1 on 2020-09-22 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desde', models.CharField(max_length=255, null=True)),
                ('hasta', models.CharField(max_length=255, null=True)),
                ('fecha_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_llegada', models.DateTimeField(default=django.utils.timezone.now)),
                ('descripcion', models.TextField(null=True)),
                ('disponibilidad', models.CharField(max_length=255, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
