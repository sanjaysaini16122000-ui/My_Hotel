from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(ModelAdmin):
    pass


