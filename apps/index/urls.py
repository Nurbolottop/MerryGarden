from django.contrib import admin
from django.urls import path

#my imports
from apps.index.views import index

urlpatterns = [
    path('', index, name ="index")
]