# Generated by Django 3.1.6 on 2021-05-19 10:22

from django.db import migrations
from django.utils.text import slugify

def add_slugs(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Post = apps.get_model("holistic", "Post")
    db_alias = schema_editor.connection.alias
    posts = Post.objects.all()
    for post in posts:
        post.slug = slugify(post.title)
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('holistic', '0006_post_slug'),
    ]

    operations = [
        migrations.RunPython(add_slugs),
    ]