from django.db import models

# Create your models here.

class Comment(models.Model):
    videoId = models.TextField(max_length=11)
    comment = models.TextField(max_length=500)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

class Reply(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, default=None)
    reply = models.TextField(max_length=500)