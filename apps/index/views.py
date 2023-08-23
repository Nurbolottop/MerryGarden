from django.shortcuts import render

# my imports
from .models import Settings

# Create your views here.

def index(request):
    setting = Settings.objects.latest('id')
    return render(request, 'index.html', locals())