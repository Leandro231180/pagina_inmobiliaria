# Generated by Django 4.0.5 on 2023-05-10 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onsale', '0013_agentes_instagram'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentes',
            name='facebook',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='agentes',
            name='linkedin',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='agentes',
            name='twiter',
            field=models.URLField(null=True),
        ),
    ]