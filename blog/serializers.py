from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post, Category


class PostSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.HyperlinkedRelatedField(many=True, view_name='category-detail', read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        field = ('created', 'title', 'author', 'content', 'categories', 'id', 'url')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = Category
        field = ('title', 'posts', 'id', 'url')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True,view_name='post-detail', read_only=True)
    essays = serializers.HyperlinkedRelatedField(many=True,view_name='essay-detail', read_only=True)

    class Meta:
        model = User
        field = ('posts', 'username', 'essays', 'id', 'url')
