from rooms.models import Room
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from rooms.models import Room
from bookings.models import Booking
from payments.models import Payment

def home(request):
    rooms = Room.objects.filter(is_active=True)
    return render(request, 'home.html', {'rooms': rooms})


@staff_member_required
def admin_dashboard(request):
    total_rooms = Room.objects.count()
    total_bookings = Booking.objects.count()
    total_payments = Payment.objects.filter(status='completed').count()
    total_revenue = sum(p.amount for p in Payment.objects.filter(status='completed'))

    recent_bookings = Booking.objects.order_by('-created_at')[:5]
    recent_payments = Payment.objects.order_by('-created_at')[:5]

    context = {
        'total_rooms': total_rooms,
        'total_bookings': total_bookings,
        'total_payments': total_payments,
        'total_revenue': total_revenue,
        'recent_bookings': recent_bookings,
        'recent_payments': recent_payments,
    }
    return render(request, 'dashboard.html', context)