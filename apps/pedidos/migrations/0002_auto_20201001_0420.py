# Generated by Django 3.1 on 2020-10-01 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='entregado',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='paquetes',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='peso',
            field=models.CharField(max_length=255, null=True),
        ),
    ]