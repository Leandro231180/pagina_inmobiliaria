# Generated by Django 4.0.5 on 2023-05-22 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onsale', '0020_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='create_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
