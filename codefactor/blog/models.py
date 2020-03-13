from django.db import models
from authentication.models import CustomUser
from django.utils.text import slugify
from markdownx.models import MarkdownxField

# Create your models here.


class Blog(models.Model):
    title = models.TextField(unique=True)
    slug_title = models.SlugField()
    location = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=True)
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    author_image = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE, related_name="Avatar")
    content = MarkdownxField(editable=True, help_text=True)
    archived = models.BooleanField(default=False)
    main_image = models.ImageField(
        upload_to='blog_images', default="images/big.png")
    thumbnail_image = models.ImageField(
        upload_to='blog_thumb_images', default="images/dummy.png")

    def save(self, *args, **kwargs):  # new
        if not self.slug_title:
            self.slug_title = slugify(self.title)
        return super().save(*args, **kwargs)


class Comments(models.Model):
    blog_title = models.ForeignKey(to=Blog, on_delete=models.CASCADE)
    comment_user_name = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE)
    comment_text = MarkdownxField(max_length=None, editable=True)

    def save(self):
        Comments.save()
