from django.contrib import admin

#my imports
from apps.team.models import Team

# Register your models here.
class TeamFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
    
admin.site.register(Team, TeamFilterAdmin)
    