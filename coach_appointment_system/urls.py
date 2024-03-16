from django.urls import path

from . import views


urlpatterns = [
    path('coach_appointment_booking', views.coach_appointment_booking, name = 'coach_appointment_booking'),
    path('coach_appointment_record', views.coach_appointment_record, name = 'coach_appointment_record')
]