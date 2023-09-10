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

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Байланыштар"
        verbose_name_plural = "Байланыш"
        