from django import forms

from .models import *
from master.models import Time


class Coach_Schedule_Form(forms.ModelForm):
    from_time  = forms.ModelChoiceField(queryset = Time.objects.all())
    to_time    = forms.ModelChoiceField(queryset = Time.objects.all())

    class Meta:
        model  = Coach_Schedule
        fields = '__all__'
    
    def clean_from_time(self):
        from_time = self.cleaned_data.get('from_time')
        if from_time:
            return from_time.time
        return None

    def clean_to_time(self):
        to_time = self.cleaned_data.get('to_time')
        if to_time:
            return to_time.time
        return None