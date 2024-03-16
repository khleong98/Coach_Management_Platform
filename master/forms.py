from django import forms

from .models import *


class Time_Form(forms.ModelForm):
    time       = forms.TimeField(input_formats = [r'%H:%M'], widget = forms.TimeInput(format = r'%H:%M', attrs = {'placeholder': 'HH:MM'}))

    class Meta:
        model  = Time
        fields = '__all__'