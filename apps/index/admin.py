from django.contrib.auth.models import User, Group
from django.contrib import admin

# my imports
from apps.index.models import Settings,Slide,Video,Services

# Register your models here.
class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class SlideFilterAdmin(admin.ModelAdmin):
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




admin.site.unregister(User)
admin.site.unregister(Group) 
admin.site.register(Settings, SettingsFilterAdmin)
admin.site.register(Slide, SlideFilterAdmin)
admin.site.register(Video, VideoFilterAdmin)
admin.site.register(Services, ServicesFilterAdmin)

