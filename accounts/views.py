# accounts/views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import Doctor, DoctorApplication
from .serializers import UserSerializer, DoctorApplicationSerializer

User = get_user_model()

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class DoctorApplicationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.is_doctor:
            return Response({"detail": "You are already a doctor."}, status=status.HTTP_400_BAD_REQUEST)
        if request.user.is_authenticated and not request.user.is_doctor:
            serializer = DoctorApplicationSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                application = serializer.save()
                # Notify superuser or handle application process
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Authentication required."}, status=status.HTTP_403_FORBIDDEN)

class ApproveDoctorView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, application_id, *args, **kwargs):
        try:
            application = DoctorApplication.objects.get(id=application_id)
            if application.status != 'Pending':
                return Response({"detail": "Application is already processed."}, status=status.HTTP_400_BAD_REQUEST)
            application.status = 'Approved'
            application.save()
            user = application.user
            user.is_doctor = True
            user.save()
            Doctor.objects.create(user=user, specialty=application.specialty, certificate=application.certificate)
            return Response({"detail": "User approved as doctor."}, status=status.HTTP_200_OK)
        except DoctorApplication.DoesNotExist:
            return Response({"detail": "Application not found."}, status=status.HTTP_404_NOT_FOUND)

class ListDoctorApplicationsView(generics.ListAPIView):
    queryset = DoctorApplication.objects.all()
    serializer_class = DoctorApplicationSerializer
    permission_classes = [permissions.IsAdminUser]
