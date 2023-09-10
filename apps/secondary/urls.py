from django.contrib import admin
from django.urls import path

#my imports
from apps.index.views import about

urlpatterns = [
    path('about', about, name ="about"),
]