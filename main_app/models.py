from django.db import models
from django.urls import reverse

class Plane(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plane-detail', kwargs={'plane_id': self.id})