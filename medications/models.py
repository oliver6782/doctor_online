from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    dosage_amount = models.CharField(max_length=255)  # e.g., "1 tablet"
    dosage_frequency = models.CharField(max_length=255)  # e.g., "Twice a day"
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.name}'