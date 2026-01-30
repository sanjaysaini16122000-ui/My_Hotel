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

            # 🔹 Availability check - only in booking view, not in admin
            available = booking.room.available_rooms(booking.check_in, booking.check_out)
            if available < 1:
                messages.error(request, f"Sorry! No rooms available for selected dates. {booking.room.total_rooms} room(s) total, but all are booked.")
                return render(request, 'bookings/create_booking.html', {'form': form})

            # total price calculation
            nights = (booking.check_out - booking.check_in).days
            booking.total_price = booking.room.price_per_night * nights
            booking.save()
            messages.success(request, "Booking created successfully!")
            return redirect('booking_success')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        room_id = request.GET.get('room_id')
        if room_id:
            form = BookingForm(initial={'room': room_id})
        else:
            form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})

