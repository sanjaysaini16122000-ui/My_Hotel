from .models import Room

def rooms_list(request):
    return {
        'nav_rooms': Room.objects.all()
    }
