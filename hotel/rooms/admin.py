from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Room

@admin.register(Room)
class RoomAdmin(ModelAdmin):
    pass

