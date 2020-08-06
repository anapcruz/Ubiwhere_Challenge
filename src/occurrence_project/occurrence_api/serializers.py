from rest_framework import serializers
from .models import Occurrence

class OccurrenceSerializer(serializers.ModelSerializer):
    #status = serializers.HiddenField(default='por_validar')
    class Meta:
        model = Occurrence
        fields = ('id', 'author', 'location', 'status','date_pub', 'date_upd','description', 'category')

        extra_kwargs = {
            'status': {'read_only': True}
        }

