from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from review.forms import ReviewForm
from review.models import Review


class ReviewCreateView(CreateView):
    """
    Создает новый экземпляр модели "Отзыв"
    """
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('review:list')


class ReviewListView(ListView):
    """
    Выводит все отзывы на страницу
    """
    model = Review


class ReviewUpdateView(UpdateView):
    """
    Позволяет изменить существующие статьи
    """
    model = Review
    form_class = ReviewForm

    # После обнавления перенаправляет на отзыв
    def get_success_url(self):
        return reverse('review:view', args=[self.kwargs.get('pk')])


class ReviewDetailView(DetailView):
    """
    Выводит статью целиком
    """
    model = Review


class ReviewDeleteView(DeleteView):
    """
    Удаляет элемент
    """
    model = Review
    success_url = reverse_lazy('review:list')
