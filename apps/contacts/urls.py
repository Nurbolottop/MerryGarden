from django.contrib import admin
from django.urls import path

#my imports
from apps.contacts.views import contact
urlpatterns = [
    path('contact/', contact, name="contact")
]