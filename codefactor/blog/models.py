from django.db import models
from authentication.models import CustomUser
from django.utils.text import slugify
from markdownx.models import MarkdownxField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug_title = models.SlugField(max_length=5, unique=True)
    location = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=True)
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    author_image = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name="Avatar")
    content = MarkdownxField(editable=True, help_text=True)
    archived = models.BooleanField(default=False)
 
    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

class Comments(models.Model):
    blog_title = models.ForeignKey(to=Blog, on_delete=models.CASCADE)
    comment_user_name = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    comment_text = MarkdownxField(max_length=None, editable=True)

    def save(self):
        Comments.save()






