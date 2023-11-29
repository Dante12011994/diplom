from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Ships(models.Model):

    """
    Модель теплохода
    """
    name = models.CharField(max_length=150, verbose_name='название теплохода')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    foto = models.ImageField(upload_to='media/', verbose_name='Фото корабля', **NULLABLE)

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'Теплоход'
        verbose_name_plural = 'Теплоходы'


class Cruise(models.Model):
    """
    Модель круиза
    """
    STATUS = [('create', 'Круиз состоится'), ('start', 'Круиз начался'), ('finished', 'Круиз завершен')]
    name = models.CharField(max_length=250, verbose_name='название круиза')
    ship = models.ForeignKey(Ships, on_delete=models.CASCADE, verbose_name='Теплоход')
    data_start = models.DateField(verbose_name='Дата начала')
    date_finish = models.DateField(verbose_name='Дата окончания')
    town_start = models.CharField(max_length=150, verbose_name='Город начала')
    town_finish = models.CharField(max_length=150, verbose_name='Город окончания')
    status_cruise = models.CharField(max_length=8, choices=STATUS, default='create')

    def __str__(self):
        return f'{self.name} начало: {self.data_start} - конец: {self.date_finish}'

    class Meta:
        verbose_name = 'Круиз'
        verbose_name_plural = 'Круизы'


class Prise(models.Model):
    """
    Модель цены
    """
    CLASS = [('standart', 'стандартная каюта'), ('deluxe', 'каюта де-люкс'), ('luxe', 'каюта люкс')]
    name = models.CharField(max_length=8, choices=CLASS, verbose_name='Класс каюты')
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE, verbose_name='Круиз')
    prise = models.PositiveIntegerField(verbose_name='Стоимость')

    def __str__(self):
        return f'{self.name}: {self.prise}'

    class Meta:
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимости'
