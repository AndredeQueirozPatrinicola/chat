import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async

from .models import *

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        room = await sync_to_async(Room.objects.get)(id=self.room_name)
        players_connected = room.players_connected
        room_limit = room.limit

        if players_connected < room_limit:
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
            await sync_to_async(Room.objects.filter(id=self.room_name).update)(players_connected=players_connected+1)
        else:
            await self.close()

    async def disconnect(self, close_code):
        room = await sync_to_async(Room.objects.get)(id=self.room_name)
        players_connected = room.players_connected

        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        await sync_to_async(Room.objects.update)(players_connected=players_connected-1)

    async def receive(self, text_data):
        payload = json.loads(text_data)
        message = payload["message"]
        user = payload["user"]

        await self.channel_layer.group_send(
            self.room_group_name, {
                                    "type": "chat_message", 
                                    "payload": {
                                        "message" : message,
                                        "user" : user
                                    }
                                  }
        )

    async def chat_message(self, event):
        message = event["payload"]["message"]
        user_id = event["payload"]['user']

        user = await sync_to_async(User.objects.get)(id=user_id)

        await self.send(text_data=json.dumps(
                                                {
                                                    "user" : {
                                                        'id' : user.id,
                                                        'username' : user.username,
                                                        'email' : user.email
                                                    },
                                                    "message": message
                                                }
                                            )
                                        )