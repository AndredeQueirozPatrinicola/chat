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
        context = super().context
        room_name = self.kwargs['room_name']
        
        messages = Chat.objects.filter(room__id=room_name)

        context['room_name'] = room_name
        context['messages'] = messages
        return context

    def get(self, *args, **kwargs):
        return render(
                 self.request, 
                "home/room.html", 
                 self.context
                )