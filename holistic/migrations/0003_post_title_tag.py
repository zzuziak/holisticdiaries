# Generated by Django 3.1.6 on 2021-05-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holistic', '0002_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='', max_length=255),
        ),
    ]
