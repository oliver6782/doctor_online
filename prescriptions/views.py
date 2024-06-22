# prescriptions/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django.core.exceptions import PermissionDenied
from accounts.models import Doctor
from .models import Prescription
from .serializers import PrescriptionSerializer
from .permissions import IsDoctorOrReadOnly, IsOwnerOrDoctorWithinTimeLimit

class PrescriptionListCreateView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated, IsDoctorOrReadOnly]
    
    

    def get_queryset(self):
        # Allow pet owners to view prescriptions for their pets
        user = self.request.user
        if user.is_authenticated and not user.is_doctor:
            return Prescription.objects.filter(pet__owner=user)
        return Prescription.objects.all()

    def perform_create(self, serializer):
        if self.request.user.is_doctor:
            doctor = Doctor.objects.get(user=self.request.user)
            serializer.save(doctor=doctor)
        else:
            raise PermissionDenied("Only doctors can create prescriptions.")

class PrescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrDoctorWithinTimeLimit]
