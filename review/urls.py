from django.urls import path

from review.apps import ReviewConfig
from review.views import ReviewCreateView, ReviewListView, ReviewUpdateView, ReviewDetailView, ReviewDeleteView

app_name = ReviewConfig.name

urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='create'),  # Создание отзыва
    path('', ReviewListView.as_view(), name='list'),  # Вывод всех отзывов
    path('edit/<int:pk>/', ReviewUpdateView.as_view(), name='edit'),  # Изменеие отзыва
    path('view/<int:pk>/', ReviewDetailView.as_view(), name='view'),  # Просмотр отзыва
    path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='delete'),  # Удаление отзыва
]
