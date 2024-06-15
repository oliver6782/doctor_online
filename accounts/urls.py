from django.urls import path
from .views import UserRegistrationView, DoctorRegistrationView

urlpatterns = [
    path('common/', UserRegistrationView.as_view(), name='common_signup'),
    path('doctor/', DoctorRegistrationView.as_view(), name='doctor_signup'),
]
