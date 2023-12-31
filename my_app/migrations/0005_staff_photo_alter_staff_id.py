# Generated by Django 4.2.1 on 2023-07-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alter_contact_us_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='photo',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
