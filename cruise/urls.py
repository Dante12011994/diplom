from django.contrib import admin
from django.urls import path

from cruise.apps import CruiseConfig
from cruise.views import main, CruiseListView

app_name = CruiseConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('cruise/', CruiseListView.as_view(), name='cruise'),
]
