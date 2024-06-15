
from django.db import models
from django.conf import settings

class Pet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField()
    medical_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
