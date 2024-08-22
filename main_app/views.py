from django.shortcuts import render

class Plane:
    def __init__(self, name, model, category, image):
        self.name = name
        self.model = model 
        self.category = category
        self.image = image

planes = [
    Plane('Seminole', 'PA-44', 'GA', 'image'),
    Plane('King Air', 'King Air 360ER', 'P', 'image'),
    Plane('Piper Warrior III', 'PA-28-151', 'GA', 'image'),
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plane_index(request):
    return render(request, 'planes/index.html', {'planes': planes})