from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from rooms.models import Room

@login_required
def add_review(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.room = room
            review.save()
            return redirect('room_detail', room_id=room.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form})
