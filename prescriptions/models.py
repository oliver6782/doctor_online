# models.py in the prescriptions app
from django.db import models
from django.conf import settings
from pets.models import Pet
from accounts.models import Doctor
from medications.models import Medication

class Prescription(models.Model):
    pet_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='prescriptions')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    medications = models.ManyToManyField(Medication, related_name='prescriptions')
    symptom_description = models.TextField(blank=True, null=True)
    diagnose = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    issued_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Prescription for {self.pet.name}'
    
    class Meta:
        unique_together = ('pet', 'issued_date')
