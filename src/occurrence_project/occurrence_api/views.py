from django.shortcuts import render
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Occurrence
from .serializers import OccurrenceSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def list_occurrence(request):
    if request.method == 'GET':
        items = Occurrence.objects.all()
        serializer = OccurrenceSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OccurrenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)