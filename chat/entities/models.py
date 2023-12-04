# entity/models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    # Add other user fields as needed

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    members = models.ManyToManyField(User)
    max_members = models.IntegerField()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add other message fields as needed
