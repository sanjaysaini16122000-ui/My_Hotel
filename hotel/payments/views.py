from django.shortcuts import render, get_object_or_404, redirect
from bookings.models import Booking
from .models import Payment

def payment_page(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Payment object create karo agar exist nahi karta
    payment, created = Payment.objects.get_or_create(
        booking=booking,
        defaults={'amount': booking.room.price_per_night}
    )

    return render(request, 'payments/payment_page.html', {
        'booking': booking,
        'payment': payment
    })

from django.views.decorators.http import require_POST

@require_POST
def payment_success(request, booking_id):
    payment = Payment.objects.get(booking_id=booking_id)
    payment.status = 'completed'
    payment.save()

    return render(request, 'payments/payment_success.html', {'payment': payment})
