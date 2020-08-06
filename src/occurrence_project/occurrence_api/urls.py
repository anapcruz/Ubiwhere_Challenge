from django.urls import path
from . import views

urlpatterns = [
    path('occurrence/', views.OccurrenceView.as_view()),
    path('occurrence/search', views.ApiOccurrenceView.as_view()),
    
]
