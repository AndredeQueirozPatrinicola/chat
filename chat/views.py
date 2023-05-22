from django.shortcuts import render
from django.views import View

from .models import *

# Create your views here.

class BaseView(View):

    @property
    def context(self):
        rooms = Room.objects.all()
        context = {"rooms" : rooms}
        return context


class IndexView(BaseView):

    def get(self, *args, **kwargs):
        return render(
                 self.request, 
                'home/index.html', 
                 self.context
                )

class RoomView(BaseView):

    @property
    def context(self):
        context = {}
        room_id = self.kwargs['room_id']
        messages = Chat.objects.filter(room__id=room_id)
        context['room_name'] = room_id
        context['messages'] = messages
        return context

    def get(self, *args, **kwargs):
        return render(
                 self.request, 
                "home/room.html", 
                 self.context
                )