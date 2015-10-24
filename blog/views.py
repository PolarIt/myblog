from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views import generic

from rest_framework import viewsets, permissions

from blog.models import Post, Category
from blog.serializers import PostSerializer, CategorySerializer, UserSerializer
from blog.permission import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provide 'create', 'update',
    'delete', 'list' actions.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provide 'create', 'update',
    'delete', 'list' actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provide 'list', 'detail' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(generic.ListView):
    model = Post
    paginate_by = 10


class PostDetail(generic.DetailView):
    model = Post
