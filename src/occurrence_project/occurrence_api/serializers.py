from rest_framework import serializers
from .models import Occurrence

class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ['id','author', 'location', 'status', 'date_pub', 'description', 'category']