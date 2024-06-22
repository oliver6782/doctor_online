# accounts/urls.py

from django.urls import path
from .views import RegisterUserView, DoctorApplicationView, ApproveDoctorView, ListDoctorApplicationsView

urlpatterns = [
    path('', RegisterUserView.as_view(), name='register_user'),
    path('doctor/', DoctorApplicationView.as_view(), name='apply_doctor'),
    path('approve/doctor/<int:application_id>/', ApproveDoctorView.as_view(), name='approve_doctor'),
    path('applications/', ListDoctorApplicationsView.as_view(), name='list_doctor_applications'),
]
