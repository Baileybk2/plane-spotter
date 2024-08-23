from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plane

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plane_index(request):
    planes = Plane.objects.all()
    return render(request, 'planes/index.html', {'planes': planes})

def plane_detail(request, plane_id):
    plane = Plane.objects.get(id=plane_id)
    return render(request, 'planes/detail.html', {'plane': plane})

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

