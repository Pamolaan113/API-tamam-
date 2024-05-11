from rest_framework import serializer
from .models import kategori,produk

class kategoriserializer(serializer.ModelSerializer):
    class meta:
        model = kategori
        fields =("id", "nama")

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", " nama", "barang",)
               