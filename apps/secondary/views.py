from django.shortcuts import render
# my imports
from apps.index.models import Settings,Video,Services
from apps.secondary.models import About,News,Gallery,List
from apps.team.models import Team
from apps.contacts.models import Reserv
from apps.contacts.views import get_text

# Create your views here.
def about(request):
    video = Video.objects.latest('id')
    services = Services.objects.all()
    setting = Settings.objects.latest('id')
    about = About.objects.latest('id')
    team = Team.objects.all()
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
    return render(request, 'about.html', locals())



def news(request):
    setting = Settings.objects.latest('id')
    news = News.objects.all()
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
    return render(request, 'news.html', locals())

def news_detail(request,id):
    setting = Settings.objects.latest('id')
    news = News.objects.get(id=id)
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
    return render(request,'post.html', locals())

def gallery(request):
    setting = Settings.objects.latest('id')
    gallery = Gallery.objects.all()
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
    return render(request, 'gallery.html', locals())

def list(request):
    setting = Settings.objects.latest('id')
    list = List.objects.latest('id')
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
    return render(request, 'list.html', locals())