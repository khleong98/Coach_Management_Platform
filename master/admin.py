from django.contrib import admin

from .forms import *
from .models import *


class Coach_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'utc',)
    ordering = ('id',)
    search_fields = ('name', 'utc',)
    list_filter = ('utc',)


class Time_Admin(admin.ModelAdmin):
    list_display = ('id', 'time',)
    ordering = ('id',)
    search_fields = ('time',)
    form = Time_Form


admin.site.register(Coach, Coach_Admin)
admin.site.register(Time, Time_Admin)