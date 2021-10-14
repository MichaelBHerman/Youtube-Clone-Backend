from rest_framework import serializers
from .models import Comment, Reply

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["videoId", "comment", "like", "dislike"]

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ["comment", "reply"]