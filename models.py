from django.db import models

class Perabot(models.Model):
  """Model untuk perabotan."""

  nama = models.CharField(max_length=255)
  deskripsi = models.TextField(blank=True)
  jenis = models.CharField(max_length=100, blank=True)  # Misal: Kursi, Meja, Lemari, dll.
  harga = models.DecimalField(max_digits=10, decimal_places=2)
  gambar = models.ImageField(upload_to='perabotan/', blank=True)  # Menyimpan gambar di folder 'perabotan/'

  def __str__(self):
    return self.nama

  class Meta:
    verbose_name = 'Perabot'
    verbose_name_plural = 'Perabotan'

