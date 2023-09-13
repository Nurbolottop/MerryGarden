from django.contrib import admin

#my imports
from apps.team.models import Team,Founder

# Register your models here.
class TeamFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class FounderFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'descriptions')
    search_fields = ('name', 'descriptions')
       
admin.site.register(Team, TeamFilterAdmin)
admin.site.register(Founder, FounderFilterAdmin)

    