from django.db import models

from cruise.models import Ships


# Create your models here.

class Review(models.Model):
    ship = models.ForeignKey(Ships, on_delete=models.SET_NULL, null=True, verbose_name='')
    text = models.TextField(verbose_name='')

    def __str__(self):
        return f'{self.ship}: {self.text}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
