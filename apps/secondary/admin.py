from django.contrib import admin

# my imports
from apps.secondary.models import About,News

# Register your models here.
class AboutFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class NewsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
    
admin.site.register(About, AboutFilterAdmin)
admin.site.register(News, NewsFilterAdmin)