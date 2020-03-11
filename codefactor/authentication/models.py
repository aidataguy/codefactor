from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    avatar = models.FileField(upload_to="avatars")
    slug = models.SlugField(null=False, unique=True)
    location = models.CharField(max_length=100, blank=True)
    about_me = models.TextField()
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

