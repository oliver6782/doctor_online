
from django.contrib import admin
from .models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'age', 'owner')
    search_fields = ('name', 'species', 'breed', 'owner__email')

admin.site.register(Pet, PetAdmin)
