from django.db import models
from django.urls import reverse
from django.utils import timezone

CATEGORY = (
    ('GA', 'General Aviation'),
    ('MI', 'Military'),
    ('AG', 'Agricultural'),
    ('SP', 'Sport'),
    ('DR', 'Drone'),
    ('GL', 'Glider')
)

class Plane(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(
        max_length=2, 
        choices=CATEGORY, 
        default=CATEGORY[0][0])
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plane-detail', kwargs={'plane_id': self.id})
    
class Sighting(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    location = models.TextField(max_length=250)
    registration = models.URLField(blank=True, null=True)
    tracking = models.URLField(blank=True, null=True)

    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)

    def __str__(self):
        return f"Spotted on {self.datetime} at {self.location}"
