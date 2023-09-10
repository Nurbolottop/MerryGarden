from django.shortcuts import render,redirect
from django.core.mail import send_mail

from apps.index.models import Settings
from apps.contacts.models import Contact
# Create your views here.
def contact(request):
    setting = Settings.objects.latest("id")
    print("KOT")
    if request.method =="POST":
        print("Work")
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name = name,email = email,message = message)
        send_mail(
            f'{message}',
            f'Добрый день {name}, спасибо за обратную связь, мы скоро свами свяжемся.Ваше обращение: {message}. Ваша  почта: {email}',
            "noreply@somehost.local",
            [email])
        return redirect('about')
    return render(request, "contact.html",locals())
