from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import BlogCreate


urlpatterns = [
    path('blog/create/', BlogCreate.as_view(), name="create_blog"),
]
