from django.urls import path
from mahasiswa import views

urlpatterns = [
    path('mahasiswa', views.mahasiswaAPI),
    path('mahasiswa/<int:id>', views.mahasiswaAPI)
]