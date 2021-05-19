from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255, default='general')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    def upper(self):
        return self.name.upper()

class Tag(models.Model):
    name = models.CharField(max_length=255, default='general')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    def upper(self):
        return self.name.upper()


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default="")
    post_summary = models.TextField(max_length=999, default="")
    body = RichTextField(blank=True, null=True)
    published = models.BooleanField(default=False)
    post_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    tag = models.ManyToManyField(Tag, related_name='tags')
    header_image = CloudinaryField('image')

    def __str__(self):
        return self.title + " | " + str(self.category)

    def get_absolute_url(self):
        # return reverse('post', args=(str(self.id)))
        return reverse('post', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.created_at.strftime('%m/%d/%Y %I:%M %p')



class Reply(models.Model):
    class Meta:
        verbose_name_plural = "Replies"

    name = models.CharField(max_length=255, default="anonymous")
    body = models.TextField()
    comments = models.ForeignKey(Comment, related_name="replies", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'
