from django.contrib import admin

from .forms import *
from .models import *


class Coach_Schedule_Admin(admin.ModelAdmin):
    list_display = ('id', 'coach', 'day', 'from_time', 'to_time',)
    ordering = ('coach', 'day', 'from_time',)
    search_fields = ('coach__name', 'day__day', 'from_time', 'to_time',)
    list_filter = ('day', 'coach',)
    form = Coach_Schedule_Form


admin.site.register(Coach_Schedule, Coach_Schedule_Admin)