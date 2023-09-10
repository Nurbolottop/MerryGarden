from django.contrib import admin

# my imports
from apps.secondary.models import About,News,Gallery

# Register your models here.
class AboutFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class NewsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class GalleryFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    list_display = ('image',)
    search_fields = ('image',)
    
admin.site.register(About, AboutFilterAdmin)
admin.site.register(Gallery, GalleryFilterAdmin)
admin.site.register(News, NewsFilterAdmin)