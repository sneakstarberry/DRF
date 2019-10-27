from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('pk', 'title', 'body', 'author_name')