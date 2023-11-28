from django.contrib import admin

from cruise.models import Ships, Cruise, Prise


# Register your models here.

@admin.register(Ships)
class Shipsadmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'description', 'foto')


@admin.register(Cruise)
class Cruiseadmin(admin.ModelAdmin):
    list_display = ("id", 'ship', 'name', 'data_start', 'date_finish')


@admin.register(Prise)
class Cruiseadmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'cruise', 'prise')
