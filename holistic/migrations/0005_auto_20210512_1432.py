# Generated by Django 3.1.6 on 2021-05-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holistic', '0004_auto_20210512_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_summary',
            field=models.CharField(default='', max_length=999),
        ),
    ]