from rest_framework import api_view
from rest_framework.response import Response
from .serializers import PostSerializer


@api_view(["GET", "POST"])
def postList(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        info = PostSerializer(data=request.data)
        info.is_valid(raise_exception=True)
        info.save()
        return Response(info.data)










