from rest_framework import serializers
from .models import Mahasiswa, History

class MahasiswaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mahasiswa
        fields = ['id', 'nim', 'nama', 'email', 'kelas', 'jurusan', 'alamat', 'no_hp']

class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ['id', 'type', 'body', 'created_at']