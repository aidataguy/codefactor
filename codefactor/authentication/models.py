from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    avatar = models.FileField(upload_to="avatars")
    slug_name = models.SlugField(max_length=50, allow_unicode=True)
    location = models.CharField(max_length=100, blank=True)
    about_me = models.TextField()
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs): # new
        if not self.slug_name:
            self.slug_name = slugify(self.name)
        return super().save(*args, **kwargs)
