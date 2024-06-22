
from django.urls import path
from .views import PetListCreateView, PetDetailView, PetListView

urlpatterns = [
    path('add/', PetListCreateView.as_view(), name='pet-list-create'),
    path('<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
    path('view/', PetListView.as_view(), name='pet-detail'),
]
