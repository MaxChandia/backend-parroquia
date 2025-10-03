from rest_framework import serializers
from .models import Post, User 

class PostSerializer(serializers.ModelSerializer):
    authorId = serializers.PrimaryKeyRelatedField(source='author', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'authorId', 'title', 'slug', 'content', 'imageUrls', 'createdAt')
        read_only_fields = ('id', 'createdAt')


class UserSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = ('id', 'user', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}
        
        