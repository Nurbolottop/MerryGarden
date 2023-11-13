from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
           
class Team(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='team/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    email = models.EmailField(
        verbose_name="Почта",
        blank=True,null=True
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    whatsapp = models.URLField(
        verbose_name='Whatspp URL',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram URL',
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name='Youtube URL',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook URL',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Наша команда"
            verbose_name_plural = "Наша команда"
            
class Founder(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='founder/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    found = models.CharField(
        max_length=255,
        verbose_name="Достижения"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    descriptions_one = models.TextField(
        verbose_name="Описание",
        blank=True,null=True
    )
    
    descriptions_two = models.TextField(
        verbose_name="Описание",
        blank=True,null=True
    )
    descriptions_three = models.TextField(
        verbose_name="Описание",
        blank=True,null=True
    )
    def __str__(self) -> str:
         return self.name
     
    class Meta:
        verbose_name = "Основатели"
        verbose_name_plural = "Основатель"
        