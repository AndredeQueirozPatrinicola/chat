from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *

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

class RoomView(LoginRequiredMixin, BaseView):
    login_url = "/login/"

    @property
    def context(self):
        room_id = self.kwargs['room_id']
        messages = Chat.objects.filter(room__id=room_id)
        return {
            'room_name' : room_id,
            "messages" : messages,
            "user_id" : self.request.user.id
        }

    def get(self, *args, **kwargs):
        players = Room.objects.filter(
                                id=self.kwargs['room_id']
                            ).values(
                                'players_connected',
                                'limit'      
                            )
        players = players[0]

        if players['players_connected'] <= players['limit']:
            return render(
                    self.request, 
                    "home/room.html", 
                    self.context
                    )
        
class CreateRoomView(LoginRequiredMixin, BaseView):
    login_url = "/login/"

    @property
    def context(self):
        form = RoomForm()
        return {"form" : form}

    def get(self, *args, **kwargs):
        return render(
                 self.request, 
                'home/create-room.html', 
                 self.context
                )

    def post(self, *args, **kwargs):

        form = RoomForm(self.request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            messages.error(self.request, "Invalid Input!")
            return redirect("/create-room")
