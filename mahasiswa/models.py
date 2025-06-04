from django.db import models

class Mahasiswa(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nim = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    nama = models.CharField(max_length=100)
    kelas = models.CharField(max_length=20)
    jurusan = models.CharField(max_length=50)
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nim} ({self.nama}) - {self.jurusan} {self.kelas}"