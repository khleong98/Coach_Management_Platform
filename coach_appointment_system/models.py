from django.db import models

from master.models import Coach, Day


class Coach_Schedule(models.Model):
    coach                   = models.ForeignKey(Coach, on_delete = models.CASCADE)
    day                     = models.ForeignKey(Day, on_delete = models.RESTRICT)
    from_time               = models.TimeField()
    to_time                 = models.TimeField()
    
    class Meta:
        verbose_name_plural = 'Coach Schedule'
        db_table            = 'cas_coach_schedule'


class Coach_Appointment(models.Model):
    coach                   = models.ForeignKey(Coach, on_delete = models.CASCADE)
    day                     = models.ForeignKey(Day, on_delete = models.RESTRICT)
    from_time               = models.DateTimeField()
    to_time                 = models.DateTimeField()
    booking_time            = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'Coach Appointment'
        db_table            = 'cas_coach_appointment'