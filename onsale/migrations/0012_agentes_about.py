# Generated by Django 4.0.5 on 2023-05-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onsale', '0011_houses_agente'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentes',
            name='about',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
