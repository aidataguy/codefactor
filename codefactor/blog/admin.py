from django.contrib import admin

# Register your models here.
from .models import Blog
class BlogUserAdmin(admin.ModelAdmin):
    model = Blog

admin.site.register(Blog, BlogUserAdmin)