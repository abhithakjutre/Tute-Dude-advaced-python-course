from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from helloapp.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloapp.models import Post
from rest_framework.permissions import IsAuthenticated
from helloapp.permissons import IsPostPossessor
from rest_framework import filters
from helloapp.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class Helloword_view(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    # queryset = Post.objects.all().order_by('-created_on')
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['title', 'body']
    ordering_fields = ['id']
    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)