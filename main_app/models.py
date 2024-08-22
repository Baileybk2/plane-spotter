from django.db import models

class Plane(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=2)
    image = models.ImageField()

    def __str__(self):
        return self.name
