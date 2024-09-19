from rest_framework import serializers
from .models import Blog, Comment, Profile


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'blog', 'user', 'content', 'created_at', 'updated_at']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    blog_count = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'blog_count', 'created_at', 'updated_at']
