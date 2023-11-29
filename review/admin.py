from django.contrib import admin

from review.models import Review


# Register your models here.
@admin.register(Review)
class Reviewadmin(admin.ModelAdmin):
    list_display = ("id", 'ship', 'owner')
