from django.urls import path
from .views import create_booking
from django.shortcuts import render


urlpatterns = [
    path('book/', create_booking, name='create_booking'),
    path('success/', lambda request: render(request, 'bookings/success.html'), name='booking_success'),
]
