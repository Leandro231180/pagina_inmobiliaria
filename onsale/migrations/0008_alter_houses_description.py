# Generated by Django 4.0.5 on 2023-05-09 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onsale', '0007_houses_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
