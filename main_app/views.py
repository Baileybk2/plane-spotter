from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Plane
from .forms import SightingForm

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def plane_index(request):
    planes = Plane.objects.all()
    return render(request, 'planes/index.html', {'planes': planes})

def plane_detail(request, plane_id):
    plane = Plane.objects.get(id=plane_id)
    sighting_form = SightingForm()
    return render(request, 'planes/detail.html', {'plane': plane, 'sighting_form': sighting_form})

class PlaneCreate(CreateView):
    model = Plane
    fields = '__all__'
    success_url = '/planes/'

class PlaneUpdate(UpdateView):
    model = Plane
    fields = ['name', 'model', 'category']

class PlaneDelete(DeleteView):
    model = Plane
    success_url = '/planes/'

def add_sighting(request, plane_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.plane_id = plane_id
        new_sighting.save()
    return redirect('plane-detail', plane_id=plane_id)