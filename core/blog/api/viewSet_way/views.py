from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PostSerializer
from blog.models import Post


class PostViewSet(viewsets.ViewSet):
    ''' class of Pso for create API action'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        ''' this class return list of post '''
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        ''' this class return details of the post '''
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def create(self, request):
        ''' this class create new data record of post '''
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)