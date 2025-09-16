from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
# Create your views here.

class Helloword_view(APIView):
    def get(self,request):
        return Response({"message": "Hello, world!"})
