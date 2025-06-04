from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from mahasiswa.models import Mahasiswa
from mahasiswa.serializers import MahasiswaSerializer
from rest_framework import generics

# Create your views here.

# @csrf_exempt
# def mahasiswaAPI(request,id=0):
#     if request.method == 'GET':
#         mahasiswa = Mahasiswa.objects.all()
#         mahasiswa_serializer = MahasiswaSerializer(mahasiswa, many=True)
#         return JsonResponse(mahasiswa_serializer.data, safe=False)
#     elif request.method == 'POST':
#         mahasiswa_data = JSONParser().parse(request)
#         mahasiswa_serializer = MahasiswaSerializer(data=mahasiswa_data)
#         if mahasiswa_serializer.is_valid():
#             mahasiswa_serializer.save()
#             return JsonResponse("Berhasil menambah data Mahasiswa", safe=False)
#     elif request.method == 'PUT':
#         mahasiswa_data = JSONParser().parse(request)
#         mahasiswa = Mahasiswa.objects.get(id=id)
#         mahasiswa_serializer = MahasiswaSerializer(mahasiswa, data=mahasiswa_data)
#         if mahasiswa_serializer.is_valid():
#             mahasiswa_serializer.save()
#             return JsonResponse("Berhasil mengubah data Mahasiswa", safe=False)
#     elif request.method == 'DELETE':
#         mahasiswa = Mahasiswa.objects.get(id=id)
#         mahasiswa.delete()
#         return JsonResponse("Berhasil menghapus data Mahasiswa", safe=False)
        

class MahasiswaCreate(generics.CreateAPIView):
    queryset = Mahasiswa.objects.all(),
    serializer_class = MahasiswaSerializer

class MahasiswaList(generics.ListAPIView):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

class MahasiswaDetail(generics.RetrieveAPIView):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

class MahasiswaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

class MahasiswaDelete(generics.RetrieveDestroyAPIView):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer