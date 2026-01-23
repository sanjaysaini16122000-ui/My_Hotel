from django import forms
from .models import Booking
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        
        if check_in and check_out:
            # Only validate dates here, not availability
            if check_in >= check_out:
                raise ValidationError("Check-out date must be after check-in date.")
        
        return cleaned_data
