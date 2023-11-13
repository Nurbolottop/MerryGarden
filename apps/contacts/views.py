from django.shortcuts import render,redirect
from django.core.mail import send_mail

from apps.index.models import Settings
from apps.contacts.models import Contact,Reserv
# Create your views here.
# BOT

from django.shortcuts import render
from django.conf import settings
from telebot import TeleBot, types

from .models import TelegramUser

# Create your views here.
bot = TeleBot(settings.TELEGRAM_TOKEN, threaded=False)
admin_id = settings.ADMIN_ID

@bot.message_handler(commands=['start'])
def start(message:types.Message):
    TelegramUser.objects.get_or_create(username = message.from_user.username, id_user=message.from_user.id, first_name = message.from_user.first_name, last_name = message.from_user.last_name,)
    # bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")

class Mail:
    def __init__(self): 
        self.description = None

mail = Mail()


def get_message(message:types.Message):
    mail.description = message.text 
    users = TelegramUser.objects.all()
    for user in users:
        bot.send_message(user.id_user, mail.description)
    bot.send_message(message.chat.id, "Рассылка окончена")

@bot.message_handler(commands=['mailing'])
def send_mailing(message:types.Message):
    if message.chat.id != int(admin_id):
        bot.send_message(message.chat.id, "Эта команда доступна только админу")
        return
    msg = bot.send_message(message.chat.id, "Введите текст для рассылки: ")
    bot.register_next_step_handler(msg, get_message)

def get_text(message):
    bot.send_message(admin_id, message)



@bot.message_handler()  
def echo(message:types.Message):
    # bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Я вас не понял")
    
    

def contact(request):
    setting = Settings.objects.latest("id")
    print("KOT")
    if request.method =="POST":
        print("Work")
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        contacts =Contact.objects.create(name = name,email = email,message = message,phone=phone)
        send_mail(
            f'{message}',
            f'Добрый день {name}, спасибо за обратную связь, мы скоро свами свяжемся.Ваше обращение: {message}. Ваша  почта: {email}',
            "noreply@somehost.local",
            [email])
        get_text(f""" Оставлено Заявка на сообщение
                 
                 
ФИО: {contacts.name}
Почта: {contacts.email}
Сообщение: {contacts.message}
Телефонный номер: {contacts.phone}
""")
        return redirect('index')
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
    return render(request, "contact.html",locals())



