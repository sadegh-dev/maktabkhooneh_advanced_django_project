from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer
from blog.models import Post


@api_view(["GET"])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        ser_data = PostSerializer(posts, many=True)
        return Response(ser_data.data)




@api_view(["GET"])
def postDetails(request, id):
    if request.method == "GET":
        posts = get_object_or_404(Post, id=id)
        ser_data = PostSerializer(posts)
        return Response(ser_data.data)


"""
@api_view(["GET"])
def postDetails(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        ser_data = PostSerializer(posts, many=True)
        return Response(ser_data.data)
    elif request.method == "POST":
        info = PostSerializer(data=request.data)
        info.is_valid(raise_exception=True)
        info.save()
        return Response(info.data)
"""





