from rest_framework import serializers
from .models import Perabot

class PerabotSerializer(serializers.ModelSerializer):
  """Serializer untuk model Perabot."""

  class Meta:
    model = Perabot
    fields = '__all__'  # Semua field dari model Perabot

class PerabotDetailSerializer(serializers.ModelSerializer):
  """Serializer detail untuk model Perabot (dengan URL gambar)."""

  gambar_url = serializers.SerializerMethodField()

  class Meta:
    model = Perabot
    fields = '__all__'  # Semua field dari model Perabot
    extra_kwargs = {'gambar': {'read_only': True}}  # gambar bersifat read-only

  def get_gambar_url(self, obj):
    """Mendapatkan URL lengkap untuk gambar perabotan."""
    request = self.context.get('request')
    if obj.gambar and hasattr(obj.gambar, 'url'):
      if request is not None:
        return request.build_absolute_uri(obj.gambar.url)  # URL absolut dengan request
      else:
        return obj.gambar.url  # URL relatif
    return None  # URL kosong jika tidak ada gambar


               