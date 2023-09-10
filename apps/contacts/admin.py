from django.contrib import admin
from apps.contacts.models import Contact,TelegramUser,Reserv
# Register your models here.

class ContactFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'chat_id', 'created']
    
    
class ReservFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')
    
admin.site.register(Reserv, ReservFilterAdmin)
admin.site.register(Contact, ContactFilterAdmin)

# Register your models here.
