from django.contrib import admin
from django.urls import path

from cruise.apps import CruiseConfig
from cruise.views import main, CruiseListView, ShipsListView, CruiseDetailView, ShipsDetailView, contact, \
    CruiseUpdateView, CruiseDeleteView, ShipsUpdateView, ShipsDeleteView

app_name = CruiseConfig.name

urlpatterns = [
    path('', main, name='main'),  # Главная страница
    path('contact/', contact, name='contact'),  # Страница контактов с возможностью отвравки сообщений
    path('cruise/', CruiseListView.as_view(), name='cruise'),  # весь список круизов
    path('ships/', ShipsListView.as_view(), name='ships'),  # весь списов теплоходов
    path('cruise/view/<int:pk>/', CruiseDetailView.as_view(), name='cruise_view'),  # просмотр отдельного круиза
    path('ships/view/<int:pk>/', ShipsDetailView.as_view(), name='ship_view'),  # просмотр отделного теплохода
    path('cruise/edit/<int:pk>/', CruiseUpdateView.as_view(), name='cruise_edit'),  # изменение круиза
    path('cruise/delete/<int:pk>/', CruiseDeleteView.as_view(), name='cruise_delete'),  # удаление круиза
    path('ships/edit/<int:pk>/', ShipsUpdateView.as_view(), name='ship_edit'),  # изменение теплохода
    path('ships/delete/<int:pk>/', ShipsDeleteView.as_view(), name='ship_delete'),  # удаление теплохода

]
