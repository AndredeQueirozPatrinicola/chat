from django.urls import path
from chat import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("chat/<str:room_id>/", views.RoomView.as_view(), name="room"),
    path("create-room", views.CreateRoomView.as_view(), name='create-room')
]
