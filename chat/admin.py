from django.contrib import admin

from .models import *

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'players_connected', 'limit')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content')
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'message')


admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat, ChatAdmin)