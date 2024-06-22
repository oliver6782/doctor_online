from django.contrib import admin
from .models import Medication

class MedicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'dosage_amount', 'dosage_frequency', 'price')
    search_fields = ('id', 'name', 'description', 'dosage_amount', 'dosage_frequency', 'price')

admin.site.register(Medication, MedicationAdmin)
