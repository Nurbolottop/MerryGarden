from django.shortcuts import render

# my imports
from .models import Settings,Slide,About,News,Video,Services,Team

# Create your views here.

def index(request):
    setting = Settings.objects.latest('id')
    slide = Slide.objects.all()
    about = About.objects.latest('id')
    news = News.objects.all()
    video = Video.objects.latest('id')
    services = Services.objects.all()
    team = Team.objects.all()
    return render(request, 'index.html', locals())