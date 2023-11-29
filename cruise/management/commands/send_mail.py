import datetime

import schedule
from django.core.management import BaseCommand

from cruise.models import Cruise


def cruise_check():
    """
    Проверяет все круизы и меняет их статус в зависимости от даты
    """
    for cruise in Cruise.objects.filter(status_cruise='create'):
        if datetime.date.today() == cruise.data_start:
            cruise.status_cruise = 'start'
    for cruise in Cruise.objects.filter(status_cruise='start'):
        if datetime.date.today() == cruise.date_finish:
            cruise.status_cruise = 'finished'


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Запуск бесконечного цикла, для проверки даты начала и окончания круиза
        """
        schedule.every().day.at("10:00").do(cruise_check)

        while True:
            schedule.run_pending()
