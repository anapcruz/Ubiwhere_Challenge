from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .modules import Occurrence
from .serializers import OccurrenceSerializer, UserCreateSerializer

class UserTestCase(APITestCase):
    
    def test_registration(self):
        data = {"username": "user100", "email": "user100@gmail.com", "password": "user_password"}
        response = self.client.post("api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)