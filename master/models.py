from django.core.validators import RegexValidator
from django.db import models


class UTC(models.Model):
    offset                  = models.CharField(max_length = 1, validators = [RegexValidator(regex = r'^[+-]$')])
    hour                    = models.TimeField()
    zone                    = models.CharField(max_length = 100, unique = True)
    
    def __str__(self):
        return f"(GMT{self.offset}{self.hour.strftime(r'%H:%M')}) {self.zone}"

    class Meta:
        verbose_name_plural = 'UTC'
        db_table            = 'master_utc'


class Day(models.Model):
    day                     = models.CharField(max_length = 9)
    
    def __str__(self):
        return self.day

    class Meta:
        verbose_name_plural = 'Day'
        db_table            = 'master_day'


class Coach(models.Model):
    name                    = models.CharField(max_length = 100)
    utc                     = models.ForeignKey(UTC, on_delete = models.RESTRICT)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Coach'
        db_table            = 'master_coach'


class Time(models.Model):
    time                    = models.TimeField(unique = True)
    
    def __str__(self):
        return self.time.strftime(r'%H:%M')

    class Meta:
        verbose_name_plural = 'Time'
        db_table            = 'master_time'