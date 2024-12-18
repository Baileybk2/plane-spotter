from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django import forms
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Plane
from .forms import SightingForm

class Login(LoginView):
    template_name = 'login.html'

def about(request):
    return render(request, 'about.html')

@login_required
def plane_index(request):
    planes = Plane.objects.filter(user=request.user)
    return render(request, 'planes/index.html', {'planes': planes})

@login_required
def plane_detail(request, plane_id):
    plane = Plane.objects.get(id=plane_id)
    sighting_form = SightingForm()
    return render(request, 'planes/detail.html', {'plane': plane, 'sighting_form': sighting_form})

class PlaneForm(forms.ModelForm):
    class Meta:
        model = Plane
        fields = ['name', 'model', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter model'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Enter category'
            }),
            'image': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image URL'
            }),
            
        }

class PlaneCreate(LoginRequiredMixin, CreateView):
    model = Plane
    form_class = PlaneForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlaneUpdate(LoginRequiredMixin, UpdateView):
    model = Plane
    form_class = PlaneForm

class PlaneDelete(LoginRequiredMixin, DeleteView):
    model = Plane
    success_url = '/planes/'

@login_required
def add_sighting(request, plane_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.plane_id = plane_id
        new_sighting.save()
    return redirect('plane-detail', plane_id=plane_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('plane-index')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = CustomUserCreationForm()

    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
