from django.shortcuts import render
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters

from .models import Occurrence
from . import serializers

class OccurrenceFiler(filters.FilterSet):
    author = filters.CharFilter(lookup_expr='icontains')
    location = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Occurrence
        fields = ('author', 'category', 'location')



class OccurrenceView(APIView):
    """Run API"""

    serializer_class = serializers.OccurrenceSerializer

    def get(self, request, format=None):
        items = Occurrence.objects.all()
        serializer = serializers.OccurrenceSerializer(items, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        """Create a new occurrence."""

        serializer = serializers.OccurrenceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiOccurrenceView(ListAPIView):
    queryset = Occurrence.objects.all()
    serializer_class = serializers.OccurrenceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OccurrenceFiler