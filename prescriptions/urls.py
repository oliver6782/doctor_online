# prescriptions/urls.py
from django.urls import path
from .views import PrescriptionListCreateView, PrescriptionDetailView

urlpatterns = [
    path('', PrescriptionListCreateView.as_view(), name='prescription_list_create'),
    path('<int:pk>/', PrescriptionDetailView.as_view(), name='prescription_detail'),
]
