from django.shortcuts import render, get_object_or_404
from .models import Room
from reviews.models import Review

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    reviews = Review.objects.filter(room=room).order_by('-created_at')

    return render(request, 'room_detail.html', {'room': room, 'reviews': reviews})
