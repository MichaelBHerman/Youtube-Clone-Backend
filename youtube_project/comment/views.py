from django.shortcuts import render
from django.http import Http404
from rest_framework import serializers
from youtube_project.comment.serializers import CommentSerializer
from .models import Comment, Reply
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CommentList (APIView):  

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)  

    def post(self, request):
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)    
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)