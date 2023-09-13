from django.contrib import admin
from django.urls import path

#my imports
from apps.secondary.views import about,news,news_detail,gallery,list

urlpatterns = [
    path('about', about, name ="about"),
    path('news', news, name ="news"),
    path('news_detail/<int:id>/', news_detail, name ="news_detail"),
    path('gallery', gallery, name ="gallery"),
    path('list', list, name ="list"),
]