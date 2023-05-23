from django import forms

from .models import *

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["owner", "name", "limit", "public"]
        labels = {'owner' : ''}
        widgets = {
            'owner' : forms.TextInput(attrs={'class' : 'hide', "id" : "owner"})
        }