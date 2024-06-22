# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Doctor, DoctorApplication

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ('user', 'specialty', 'certificate')

class DoctorApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorApplication
        fields = ('user', 'specialty', 'certificate', 'status', 'applied_at')
        read_only_fields = ('status', 'applied_at')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        application = DoctorApplication.objects.create(**validated_data)
        return application
