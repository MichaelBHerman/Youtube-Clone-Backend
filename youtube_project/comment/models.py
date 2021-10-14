from django.db import models

# Create your models here.

class Comment(models.Model):
    videoId = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, default=None)
    reply = models.CharField(max_length=500)