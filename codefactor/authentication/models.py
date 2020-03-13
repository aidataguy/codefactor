from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    slug_name = models.SlugField(max_length=50, allow_unicode=True)
    location = models.CharField(max_length=100, blank=True)
    about_me = models.TextField(blank=True)
    status = models.BooleanField(default=True)
