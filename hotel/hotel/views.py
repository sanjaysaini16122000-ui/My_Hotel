from django.shortcuts import render
from rooms.models import Room


def home(request):
    rooms = Room.objects.filter(is_active=True)
    return render(request, 'home.html', {'rooms': rooms})
