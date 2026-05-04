from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Review

@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ('user', 'room', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
