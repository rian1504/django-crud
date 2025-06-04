from rest_framework import serializers
from .models import Mahasiswa

class MahasiswaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mahasiswa
        fields = ['id', 'nim', 'nama', 'email', 'kelas', 'jurusan', 'alamat', 'no_hp']