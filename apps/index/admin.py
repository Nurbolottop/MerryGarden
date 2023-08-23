from django.contrib.auth.models import User, Group
from django.contrib import admin
# my imports

from .models import Settings,Slide,About,News,Video,Services,Team

# Register your models here.
class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class AboutFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class NewsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class VideoFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)

class ServicesFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

class TeamFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')


admin.site.unregister(User)
admin.site.unregister(Group) 
admin.site.register(Settings, SettingsFilterAdmin)
admin.site.register(Slide, SlideFilterAdmin)
admin.site.register(About, AboutFilterAdmin)
admin.site.register(News, NewsFilterAdmin)
admin.site.register(Video, VideoFilterAdmin)
admin.site.register(Services, ServicesFilterAdmin)
admin.site.register(Team, TeamFilterAdmin)

