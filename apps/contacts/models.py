from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Запросы на связи"
        verbose_name_plural = "Запросы на связь"
        
        

# Create your models here.
class TelegramUser(models.Model):
    id_user = models.CharField(
        max_length=100,
        verbose_name="ID пользователя telegram"
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя",
        blank=True, null=True
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        blank=True, null=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия",
        blank=True, null=True
    )
    chat_id = models.CharField(
        max_length=100,
        verbose_name="Чат ID"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )

    def __str__(self):
        return str(self.username)
    
    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграма"
        
class Reserv(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    date  = models.CharField(
        max_length=255,
        verbose_name= "Дата"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    class Meta:
        verbose_name = 'Брони'
        verbose_name_plural = "Бронь"