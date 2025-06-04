from django.urls import path
from mahasiswa import views

urlpatterns = [
    # path('mahasiswa', views.mahasiswaAPI),
    # path('mahasiswa/<int:id>', views.mahasiswaAPI)

    path('create', views.MahasiswaCreate.as_view(), name='create-mahasiswa'),
    path('', views.MahasiswaList.as_view()),
    path('<int:pk>', views.MahasiswaDetail.as_view(), name='detail-mahasiswa'),
    path('update/<int:pk>', views.MahasiswaUpdate.as_view(), name='update-mahasiswa'),
    path('delete/<int:pk>', views.MahasiswaDelete.as_view(), name='delete-mahasiswa'),
    path('history', views.HistoryList.as_view()),
]