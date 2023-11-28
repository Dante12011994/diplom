from django.shortcuts import render
from django.views.generic import ListView

from cruise.models import Cruise, Ships


def main(request):
    cruise_list = Cruise.objects.filter(status_cruise='create')
    ship_list = Ships.objects.all()
    context = {
        "cruise_list": cruise_list,
        "ship_list": ship_list
    }
    return render(request, 'cruise/main.html', context)


class CruiseListView(ListView):
    """
    Отображение всех круизов
    """
    model = Cruise
