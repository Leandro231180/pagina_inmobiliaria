# Generated by Django 4.0.5 on 2023-05-09 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onsale', '0009_agentes'),
    ]

    operations = [
        migrations.AddField(
            model_name='onsale',
            name='Agente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='onsale.agentes'),
        ),
    ]
