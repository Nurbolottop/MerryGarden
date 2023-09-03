from django.contrib import admin
from django.urls import path

#my imports
from apps.index.views import index,about

urlpatterns = [
    path('', index, name ="index"),
    path('about', about, name ="about"),
    
]