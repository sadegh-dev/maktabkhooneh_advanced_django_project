from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PostSerializer, CategorySerializer
from blog.models import Category, Post


class CategoryModelViewSet(viewsets.ModelViewSet) :
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PostModelViewSet(viewsets.ModelViewSet) :
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

