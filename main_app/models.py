from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plane-detail', kwargs={'plane_id': self.id})