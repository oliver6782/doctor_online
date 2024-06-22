# prescriptions/permissions.py
from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone

class IsDoctorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access to all users
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Allow create, update, delete access only to doctors
        return request.user.is_authenticated and request.user.is_doctor

class IsOwnerOrDoctorWithinTimeLimit(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only access to pet owners
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return obj.pet.owner == request.user
        
        # Allow update and delete access only to the doctor who created the prescription within 2 hours
        if request.user.is_authenticated and request.user.is_doctor and obj.doctor == request.user:
            time_limit = obj.created_at + timedelta(hours=2)
            return timezone.now() <= time_limit
        
        return False
