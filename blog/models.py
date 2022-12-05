from django.conf import settings
from django.db import models
from store.models import Customer
from django.urls import reverse
from store.models import Product
from django_resized import ResizedImageField
from django.utils.text import slugify
from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO

image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
}

class Tag(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post')
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE, related_name='post')
    tags = models.ManyToManyField(Tag, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=1500)
    slogan = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='post_images')

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='comments')
    message = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author}'s comment"

