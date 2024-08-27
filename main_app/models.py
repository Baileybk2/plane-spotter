from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User

CATEGORY = (
    ('GA', 'General Aviation'),
    ('CM', 'Commercial'),
    ('MI', 'Military'),
    ('PR', 'Private'),
    ('CP', 'Corporate'),
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
    image = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plane-detail', kwargs={'plane_id': self.id})
    
class Sighting(models.Model):
    datetime = models.DateTimeField(default=timezone.now, verbose_name='Sighting date')
    location = models.TextField(max_length=250)
    registration = models.CharField(max_length=10, blank=True, null=True)
    tracking = models.URLField(blank=True, null=True)

    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)

    def __str__(self):
        return f"Spotted on {self.datetime} at {self.location}"
    
    class Meta:
        ordering = ['-datetime']
