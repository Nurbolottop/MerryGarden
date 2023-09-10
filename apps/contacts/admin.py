from django.contrib import admin
from apps.contacts.models import Contact
# Register your models here.

class ContactFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    
admin.site.register(Contact, ContactFilterAdmin)

# Register your models here.
