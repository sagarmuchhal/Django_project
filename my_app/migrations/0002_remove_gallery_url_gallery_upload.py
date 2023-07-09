# Generated by Django 4.2.1 on 2023-07-08 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='url',
        ),
        migrations.AddField(
            model_name='gallery',
            name='upload',
            field=models.ImageField(default=datetime.datetime(2023, 7, 8, 19, 25, 39, 639127), upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
