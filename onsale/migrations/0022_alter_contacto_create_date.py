# Generated by Django 4.0.5 on 2023-05-22 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onsale', '0021_contacto_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
