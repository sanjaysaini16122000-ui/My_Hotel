from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    list_display = ('id', 'booking', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('booking__id',)
    readonly_fields = ('created_at',)
