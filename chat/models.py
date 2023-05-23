import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=False)
    players_connected = models.IntegerField(null=False)
    limit = models.IntegerField(null=False)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)    
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return self.room.name

