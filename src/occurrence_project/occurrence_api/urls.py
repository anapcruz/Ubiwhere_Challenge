from django.urls import path
from . import views

urlpatterns = [
    path('occurrence/', views.list_occurrence),
    
]
