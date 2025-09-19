from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from helloapp.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloapp.models import Post
# Create your views here.

class Helloword_view(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer