from django.shortcuts import render
from django.http import Http404
from rest_framework import serializers
from .serializers import CommentSerializer, ReplySerializer
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
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplyList (APIView):  

    def get(self, request):
        reply = Reply.objects.all()
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)  

    def post(self, request):
        serializer = ReplySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
