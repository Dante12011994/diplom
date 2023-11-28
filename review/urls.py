from django.urls import path

from review.apps import ReviewConfig
from review.views import ReviewCreateView, ReviewListView, ReviewUpdateView, ReviewDetailView, ReviewDeleteView

app_name = ReviewConfig.name

urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='create'),  # Создание статьи
    path('', ReviewListView.as_view(), name='list'),  # Вывод всех статей
    path('edit/<int:pk>/', ReviewUpdateView.as_view(), name='edit'),  # Изменеие статьи
    path('view/<int:pk>/', ReviewDetailView.as_view(), name='view'),  # Просмотр статьи
    path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='delete'),  # Удаление статьи
]
