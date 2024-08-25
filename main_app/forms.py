from django import forms
from .models import Sighting

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = ['datetime', 'location', 'registration', 'tracking']
        widgets = {
           'datetime': forms.DateTimeInput(
                format=('%Y-%m-%dT%H:%M'),
                attrs={
                    'placeholder': 'Select a date and time',
                    'type': 'datetime-local',
                }
           ),
        }
