# Create your models here.
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    description = models.TextField()
    rating = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


