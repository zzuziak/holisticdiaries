# Generated by Django 3.1.6 on 2021-05-13 18:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holistic', '0008_auto_20210513_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
