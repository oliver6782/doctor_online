
from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'owner', 'name', 'species', 'breed', 'age', 'medical_conditions']
        read_only_fields = ['id', 'owner']
