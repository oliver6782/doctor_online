from django.urls import path
from .views import MedicationDetail, MedicationList, MedicationListCreate

urlpatterns = [
    path('add/', MedicationListCreate.as_view(), name='medication-list-create'),
    path('<int:pk>/', MedicationDetail.as_view(), name='medication-detail'),
    path('view/', MedicationList.as_view(), name='medication-view'),
]