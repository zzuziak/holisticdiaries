# Generated by Django 3.1.6 on 2021-05-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holistic', '0010_delete_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]