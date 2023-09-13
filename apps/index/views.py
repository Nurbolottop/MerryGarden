from django.shortcuts import render,redirect


# my imports
from apps.index.models import Settings,Slide,Video,Services
from apps.secondary.models import About,News
from apps.team.models import Team,Founder
from apps.contacts.models import Reserv
from apps.contacts.views import get_text
# Create your views here.

def index(request):
    setting = Settings.objects.latest('id')
    slide = Slide.objects.all()
    about = About.objects.latest('id')
    news = News.objects.all()
    video = Video.objects.latest('id')
    services = Services.objects.all()
    team = Team.objects.all()
    founder = Founder.objects.latest('id')
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        message = request.POST.get('message')
        reserv = Reserv.objects.create(name = name,phone = phone,date = date,message=message)
        get_text(f""" Оставлен бронь✅
                 
                 
ФИО: {reserv.name}
Телефонный номер: {reserv.phone}
Дата: {reserv.date}
Сообщение: {reserv.message}
""")
    return render(request, 'index.html', locals())
