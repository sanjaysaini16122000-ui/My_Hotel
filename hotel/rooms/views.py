from django.shortcuts import render, get_object_or_404
from .models import Room

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room_detail.html', {'room': room})
