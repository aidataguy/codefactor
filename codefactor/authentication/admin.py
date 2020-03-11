from django.contrib import admin

# Register your models here.
from .models import CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    prepopulated_fields = { 'slug': ['name']}

admin.site.register(CustomUser, CustomUserAdmin)