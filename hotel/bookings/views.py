from django.shortcuts import render, redirect
from .forms import BookingForm
from rooms.models import Room
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # logged-in user

            # 🔹 Availability check
            available = booking.room.available_rooms(booking.check_in, booking.check_out)
            if available < 1:
                messages.error(request, "Sorry! No rooms available for selected dates.")
                return render(request, 'bookings/create_booking.html', {'form': form, 'booking': booking})

            # total price calculation
            nights = (booking.check_out - booking.check_in).days
            booking.total_price = booking.room.price_per_night * nights
            booking.save()
            return redirect('payment_page', booking_id=booking.id)
    else:
        room_id = request.GET.get('room_id')
        if room_id:
            form = BookingForm(initial={'room': room_id})
        else:
            form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})

