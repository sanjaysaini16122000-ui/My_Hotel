from django.db import models
from hotels.models import Hotel
class Room(models.Model):
    ROOM_TYPE_CHOICES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
    )

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    total_rooms = models.PositiveIntegerField()
    amenities = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='rooms/', null=True, blank=True)

    def __str__(self):
        return f"{self.room_type}"

    def available_rooms(self, check_in, check_out):
        """
        Returns number of rooms available for given dates
        """
        from bookings.models import Booking
        booked_count = Booking.objects.filter(
            room=self,
            status__in=['pending', 'confirmed'],
            check_in__lt=check_out,
            check_out__gt=check_in
        ).count()
        return self.total_rooms - booked_count

from django.db.models import Avg

def average_rating(self):
    return self.reviews.aggregate(avg=Avg('rating'))['avg'] or 0