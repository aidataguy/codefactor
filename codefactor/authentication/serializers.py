from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser
class TokenPairSerializers(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(TokenPairSerializers, cls).get_token(user)

        # add custom claims
        token['name'] = user.slug_name
        return token

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required= True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)


    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data) 
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
