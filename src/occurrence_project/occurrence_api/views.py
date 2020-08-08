from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model
from rest_framework_gis.filters import DistanceToPointFilter
from .models import Occurrence
from . import serializers


User = get_user_model()

class OccurrenceFiler(filters.FilterSet):
    author = filters.CharFilter(lookup_expr='icontains')
    address = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Occurrence
        fields = ('author', 'category', 'address')



class OccurrenceView(ListAPIView):
    """List and create occurrences."""
    queryset = Occurrence.objects.all()
    serializer_class = serializers.OccurrenceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OccurrenceFiler

    #serializer_class = serializers.OccurrenceSerializer

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
    """Filter by author, category and location."""
    queryset = Occurrence.objects.all()
    serializer_class = serializers.OccurrenceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OccurrenceFiler


class UserCreateView(CreateAPIView):
    """Create user."""
    serializer_class = serializers.UserCreateSerializer
    queryset = User.objects.all()
