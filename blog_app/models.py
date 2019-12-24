from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse("blog_app:blog_detail", kwargs={'pk': self.pk})
