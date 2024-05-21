from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Perabotan
from .serializers import PerabotanSerializer

@api_view(['GET', 'POST'])
def perabotan_list(request):
    """
    List semua perabotan atau buat perabotan baru.
    """
    if request.method == 'GET':
        perabotan = Perabotan.objects.all()
        serializer = PerabotanSerializer(perabotan, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PerabotanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def perabotan_detail(request, pk):
    """
    Retrieve, update or delete a perabotan instance.
    """
    try:
        perabotan = Perabotan.objects.get(pk=pk)
    except Perabotan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PerabotanSerializer(perabotan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PerabotanSerializer(perabotan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        perabotan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

