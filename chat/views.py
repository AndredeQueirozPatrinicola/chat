from django.shortcuts import render

# Create your views here.


def index(request):
    rooms = [
        {
            "name" : "Room 1",
            "number" : "1"
        },
        {
            "name" : "Room 2",
            "number" : "2"
        },
        {
            "name" : "Room 3",
            "number" : "3"
        },
    ]

    return render(request, 'home/index.html', {"rooms" : rooms})

def room(request, room_name):
    return render(request, "home/room.html", {"room_name": room_name})