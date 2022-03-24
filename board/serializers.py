from .models import Post, Comment
from rest_framework import serializers



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'created_dt', 'comment']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('pk', 'title', 'author', 'body', 'created_dt', 'updated_dt', 'comments')
        # fields = '__all__'
