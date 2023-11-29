from django.conf import settings
from django.db import models

from cruise.models import Ships, NULLABLE


# Create your models here.

class Review(models.Model):
    """
    Модель отзывов о теплоходе
    """
    ship = models.ForeignKey(Ships, on_delete=models.SET_NULL, null=True, verbose_name='Теплоход')
    text = models.TextField(verbose_name='Отзыв')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.ship}: {self.text}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
