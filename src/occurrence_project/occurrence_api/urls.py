from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('occurrence/', views.OccurrenceView.as_view()),
    path('occurrence/search', views.ApiOccurrenceView.as_view()),
    
]
