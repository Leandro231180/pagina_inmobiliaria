# Generated by Django 4.0.5 on 2023-05-10 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onsale', '0012_agentes_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentes',
            name='instagram',
            field=models.URLField(null=True),
        ),
    ]