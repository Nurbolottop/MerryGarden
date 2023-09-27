from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип",
        blank = True, null = True
    )
    descriptions_contacts = models.TextField(
        verbose_name="Описание для страницы 'Контакты' ",
        blank=True,null=True
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Телефон номер'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта'
        )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес'
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
    telegram_token = models.CharField(
        max_length=255,
        verbose_name="Телеграм токен"
    )
    admin_token = models.CharField(
        max_length=255,
        verbose_name="Админ айди"
    )
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Основная настройка"
            verbose_name_plural = "Основные настройки"
            
class Slide(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='slide/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    title  = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Слайд на главной странице"
            verbose_name_plural = "Слайды на главной странице"
            
class Video(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='video/',
        verbose_name="Фотография для баннера",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название видео",
        blank=True,null=True
    )
    url = models.URLField(
        verbose_name="Ссылка на видео",
        blank=True,null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Видео о MerriGarden"
            verbose_name_plural = "Видео о MerriGarden"
            
class Services(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='services/',
        verbose_name="Фотография услуги",
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
            verbose_name = "Услуга"
            verbose_name_plural = "Услуги"
 