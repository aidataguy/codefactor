from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Blog


class TokenPairSerializers(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(TokenPairSerializers, cls).get_token(user)

        # add custom claims
        token['name'] = user.slug_name
        return token


class BlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required=True
    )

    class Meta:
        model = Blog
        fields = ['title', 'slug_title', 'location', 'author', 'status',
                  'author_image', 'content', 'main_image',  'thumbnail_image']

    def create(self, validated_data):
        title = validated_data.pop("title", None)
        instance = self.Meta.model()
        if title is not None:
            instance.title(title)
        instance.save()
        return instance
