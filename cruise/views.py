from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from cruise.forms import CruiseForm, ShipForm
from cruise.models import Cruise, Ships


def main(request):
    cruise_list = Cruise.objects.filter(status_cruise='create').order_by('?')[:3]
    ship_list = Ships.objects.order_by('?')[:3]
    context = {
        "cruise_list": cruise_list,
        "ship_list": ship_list
    }
    return render(request, 'cruise/main.html', context)


def contact(request):
    """
    Обрабатывает действия на странице "Контакты"
    """
    # Принимает информацию сообщения оставленого пользователем
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('massage')

        # Воводит сообщение в консоль
        print(f'{name} ({email}): {text}')
    return render(request, 'cruise/contact.html')


class CruiseListView(ListView):
    """
    Отображение всех круизов
    """
    model = Cruise


class ShipsListView(ListView):
    model = Ships


class CruiseDetailView(DetailView):
    """
    Выводит информацию о круизе
    """
    model = Cruise


class ShipsDetailView(DetailView):
    """
    Выводит информацию о теплоходе
    """
    model = Ships


class CruiseUpdateView(UpdateView):
    """
    Позволяет изменить круиз
    """
    model = Cruise
    form_class = CruiseForm

    # После обнавления перенаправляет на круиз
    def get_success_url(self):
        return reverse('cruise:cruise_view', args=[self.kwargs.get('pk')])


class CruiseDeleteView(DeleteView):
    """
    Удаляет круиз
    """
    model = Cruise
    success_url = reverse_lazy('cruise:cruise')


class ShipsUpdateView(UpdateView):
    """
    Позволяет изменить теплоход
    """
    model = Ships
    form_class = ShipForm

    # После обнавления перенаправляет на теплоходы
    def get_success_url(self):
        return reverse('cruise:ship_view', args=[self.kwargs.get('pk')])


class ShipsDeleteView(DeleteView):
    """
    Удаляет теплоход
    """
    model = Ships
    success_url = reverse_lazy('cruise:ships')
