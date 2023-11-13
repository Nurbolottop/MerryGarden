from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class News(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='news/',
        verbose_name="Новости",
        blank = True, null = True
    )

    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Новость"
            verbose_name_plural = "Новости"
            
class About(models.Model):
    image_1 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='about/',
        verbose_name="Первая фотография",
        blank = True, null = True
    )
    image_2 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='about/',
        verbose_name="Вторая фотография",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Информация о нас"
            verbose_name_plural = "Информации о нас"
            
            
class Gallery(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='gallery/',
        verbose_name="фотография",
        blank = True, null = True
    )
    
    class Meta:
            verbose_name = "Галерея"
            verbose_name_plural = "Галерея"
            
class List(models.Model):
    image_one = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='price/',
        verbose_name="Первая фотография",
        blank = True, null = True
    )
    image_two = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='price/',
        verbose_name="Первая фотография",
        blank = True, null = True
    )
    class Meta:
            verbose_name = "Прайс"
            verbose_name_plural = "Прайс"
            