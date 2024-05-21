from rest_framework import serializers
from .models import Perabotan

class PerabotanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perabotan
        fields = ['id', 'nama', 'jenis', 'harga', 'deskripsi']
class PenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = ['id', 'nama', 'email', 'alamat']
class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaksi
        fields = ['id', 'perabotan', 'pengguna', 'tanggal', 'jumlah']        