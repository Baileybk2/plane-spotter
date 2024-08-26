from django import forms
from .models import Sighting
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
                    'class': 'form-control',
                }
           ),
           'location': forms.TextInput(
               attrs={
                   'placeholder': 'Enter location',
                   'class': 'form-control',
               }
           ),
           'registration': forms.TextInput(
               attrs={
                   'placeholder': 'Enter registration',
                   'class': 'form-control',
               }
           ),
           'tracking': forms.URLInput(
               attrs={
                   'placeholder': 'Enter tracking URL (optional)',
                   'class': 'form-control',
               }
           )
        }

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password cannot exceed 16 letters or numbers'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            })
        }