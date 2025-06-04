from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Mahasiswa, History

# Variabel sementara untuk menyimpan nama lama
_old_nama_cache = {}

@receiver(pre_save, sender=Mahasiswa)
def cache_old_nama(sender, instance, **kwargs):
    if instance.pk:  # Jika objek sudah ada di DB
        try:
            old_instance = Mahasiswa.objects.get(pk=instance.pk)
            _old_nama_cache[instance.pk] = old_instance.nama
        except Mahasiswa.DoesNotExist:
            _old_nama_cache[instance.pk] = None

@receiver(post_save, sender=Mahasiswa)
def mahasiswa_saved(sender, instance, created, **kwargs):
    if created:
        History.objects.create(
            type='create',
            body=f'Data Mahasiswa dengan nama {instance.nama} telah dibuat'
        )
    else:
        old_nama = _old_nama_cache.pop(instance.pk, None)
        if old_nama and old_nama != instance.nama:
            History.objects.create(
                type='update',
                body=f'Nama Mahasiswa berubah dari {old_nama} menjadi {instance.nama}'
            )
        else:
            History.objects.create(
                type='update',
                body=f'Data Mahasiswa dengan nama {instance.nama} telah diperbarui'
            )

@receiver(post_delete, sender=Mahasiswa)
def mahasiswa_deleted(sender, instance, **kwargs):
    History.objects.create(
        type='delete',
        body=f'Data Mahasiswa dengan nama {instance.nama} telah dihapus'
    )
