from django.contrib import admin
from django.urls import path

#my imports
from apps.team.views import team

urlpatterns = [
    path('team', team, name ="team"),
    
]