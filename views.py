from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # Opsional: Hanya user terautentikasi yang bisa edit/hapus

from .models import Perabot
from .serializers import PerabotSerializer, PerabotDetailSerializer

class PerabotList(APIView):
  """List dan create perabotan."""

  permission_classes = [IsAuthenticatedOrReadOnly]  # Opsional: Hanya user terautentikasi yang bisa create

  def get(self, request):
    """Menampilkan daftar perabotan."""
    perabotan = Perabot.objects.all()
    serializer = PerabotSerializer(perabotan, many=True)
    return Response(serializer.data)

  def post(self, request):
    """Membuat perabotan baru."""
    serializer = PerabotSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)  # Created
    return Response(serializer.errors, status=400)  # Bad Request

class PerabotDetail(APIView):
  """Detail, update, dan delete perabotan."""

  permission_classes = [IsAuthenticatedOrReadOnly]  # Opsional: Hanya user terautentikasi yang bisa edit/hapus

  def get_object(self, pk):
    """Mendapatkan objek perabotan berdasarkan ID."""
    try:
      return Perabot.objects.get(pk=pk)
    except Perabot.DoesNotExist:
      return None

  def get(self, request, pk):
    """Menampilkan detail perabotan."""
    perabot = self.get_object(pk)
    if not perabot:
      return Response(status=404)  # Not Found
    serializer = PerabotDetailSerializer(perabot, context={'request': request})  # Tambahkan request untuk URL absolut
    return Response(serializer.data)

  def put(self, request, pk):
    """Update perabotan."""
    perabot = self.get_object(pk)
    if not perabot:
      return Response(status=404)  # Not Found
    serializer = PerabotDetailSerializer(perabot, data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=400)  # Bad Request

  def delete(self, request, pk):
    """Hapus perabotan."""
    perabot = self.get_object(pk)
    if not perabot:
      return Response(status=404)  # Not Found
    perabot.delete()
    return Response(status=204)  # No Content

