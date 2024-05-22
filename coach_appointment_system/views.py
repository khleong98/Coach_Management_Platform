from datetime import datetime, timedelta
from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect, render

from .models import *
from master.models import Coach, Time


'''
================================================================================
This module facilitates the booking of appointments with coaches. Users can view
coach schedules and make appointments with them. By default, appointments have a
duration of 30 minutes and are assumed to be one-on-one sessions. The system
validates appointment times to ensure they align with the chosen coach's
schedule and do not conflict with existing appointments. With the potential
setup of user authentication in the future, the module will enable bookings to
be made while considering the time zones between the user and the coach.
================================================================================
'''

@transaction.atomic
def coach_appointment_booking(request):
    
    if request.method == 'GET':

        coach_schedule = [{'coach': i.coach, 'utc': i.coach.utc, 'day': i.day, 'from_time': i.from_time, 'to_time': i.to_time} for i in Coach_Schedule.objects.all().order_by('coach', 'day_id', 'from_time')]
        
        coach_option = list({i['coach'] for i in coach_schedule})
        time_option = [i.strftime(r'%H:%M') for i in Time.objects.values_list('time', flat = True).order_by('time')]
        
        context = {'coach'         : coach_option,
                   'time'          : time_option,
                   'coach_schedule': coach_schedule}
        
        return render(request, 'coach_appointment_booking.html', context = context)
    
    else:
        
        coach = request.POST.get('coach')
        date = request.POST.get('date')
        time = request.POST.get('time')

        coach_id = Coach.objects.filter(name = coach).first().id
        from_appointment_time = datetime.strptime(f'{date} {time}', r'%Y-%m-%d %H:%M')
        to_appointment_time = from_appointment_time + timedelta(minutes = 30)
        appointment_day_id = from_appointment_time.weekday() + 1
        
        coach_schedule = [{'from_time': i.from_time, 'to_time': i.to_time} for i in Coach_Schedule.objects.filter(coach_id = coach_id, day_id = appointment_day_id).all()]

        for schedule in coach_schedule:

            if schedule['from_time'] <= from_appointment_time.time() and schedule['to_time'] >= to_appointment_time.time():

                present_appointment = [{'from_time': i.from_time + timedelta(hours = 8), 'to_time': i.to_time + timedelta(hours = 8)} for i in Coach_Appointment.objects.filter(coach_id = coach_id, from_time__date = from_appointment_time.date()).all()]

                for appointment in present_appointment:
                    if appointment['from_time'].time() <= from_appointment_time.time() < appointment['to_time'].time() or appointment['from_time'].time() < to_appointment_time.time() <= appointment['to_time'].time():
                        messages.error(request, f'Your appointment with {coach} clashes with other existing.')
                        return redirect('coach_appointment_booking')
                
                coach_appointment_table = Coach_Appointment(coach_id = coach_id, day_id = appointment_day_id, from_time = from_appointment_time, to_time = to_appointment_time)
                coach_appointment_table.save()
                
                messages.success(request, f'Your appointment with {coach} is booked successfully!')
                return redirect('coach_appointment_record')
        
        messages.error(request, f"Your appointment does not match with {coach}'s schedule.")
        return redirect('coach_appointment_booking')


'''
================================================================================
This module is responsible for managing and displaying past appointment bookings
with coaches. In anticipation of future deployment of user authentication
measures, the module is designed to ensure that appointment records are only
accessible to the respective authenticated users, thereby safeguarding privacy
and data security.
================================================================================
'''

def coach_appointment_record(request):

    coach_appointment = [{'coach': i.coach, 'utc': i.coach.utc, 'from_time': i.from_time, 'to_time': i.to_time, 'day': i.day, 'booking_time': i.booking_time} for i in Coach_Appointment.objects.all().order_by('-from_time')]

    context = {'coach_appointment': coach_appointment}

    return render(request, 'coach_appointment_record.html', context = context)
