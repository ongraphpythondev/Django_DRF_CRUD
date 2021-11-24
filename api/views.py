from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from api.models import Comment
from api.serializers import CommentSerializer

# Create your views here.


class CommentListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    
    def get(self, request):
        comment = Comment.objects.filter(user = request.user.id)
        serializer = CommentSerializer(Comment.objects.all() ,many = True)
        return Response(serializer.data , status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

        