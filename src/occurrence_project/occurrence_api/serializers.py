from rest_framework import serializers
from rest_framework.serializers import ValidationError
from django.contrib.auth import get_user_model
from .models import Occurrence
from rest_framework_gis.serializers import GeoFeatureModelSerializer

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'            
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("A user with this email address has already registered.")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username = username,
            email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class OccurrenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Occurrence
        fields = ('id', 'author', 'address', 'status','date_pub', 'date_upd','description', 'category')

        extra_kwargs = {
            'status': {'read_only': True},
            #'location': {'read_only': True}
        }
    
    def validate(self, data):
        name = data['author']
        user_qs = User.objects.filter(username=name)
        print("name: " + name)
        print("user_qs: " + str(user_qs))

        if user_qs.exists():
            return data
            
        raise ValidationError("The user does not be registered.")
        

    def create(self, validated_data):
        name = validated_data['author']
        address = validated_data['address']
        description = validated_data['description']
        category = validated_data['category']

        occurrence_obj = Occurrence(
            author = name,
            address = address,
            description = description,
            category = category
        )
        occurrence_obj.save()
        return validated_data

