# serializers.py
from rest_framework import serializers
from .models import Prescription
from medications.serializers import MedicationSerializer
from medications.models import Medication

class PrescriptionSerializer(serializers.ModelSerializer):
    medications = MedicationSerializer(many=True)

    class Meta:
        model = Prescription
        fields = [
            'id', 'pet_owner', 'pet', 'doctor', 'medications',
            'symptom_description', 'diagnose', 'instructions',
            'issued_date', 'expiry_date', 'created_at'
        ]
        extra_kwargs = {
            'pet_owner': {'required': True},
            'pet': {'required': True},
            'diagnose' : {'required': True},
        }
        read_only_fields = ['pet_owner', 'doctor']

    def create(self, validated_data):
        medications_data = validated_data.pop('medications')
        prescription = Prescription.objects.create(**validated_data)
        for medication_data in medications_data:
            medication, created = Medication.objects.get_or_create(**medication_data)
            prescription.medications.add(medication)
        return prescription

    def update(self, instance, validated_data):
        medications_data = validated_data.pop('medications')
        instance.symptom_description = validated_data.get('symptom_description', instance.symptom_description)
        instance.diagnose = validated_data.get('diagnose', instance.diagnose)
        instance.instructions = validated_data.get('instructions', instance.instructions)
        instance.expiry_date = validated_data.get('expiry_date', instance.expiry_date)
        instance.save()

        instance.medications.clear()
        for medication_data in medications_data:
            medication, created = Medication.objects.get_or_create(**medication_data)
            instance.medications.add(medication)

        return instance
