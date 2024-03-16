Welcome to the Coach Management Platform! This platform serves as a centralized hub for managing coach-related activities, aiming for enhanced extensibility to accommodate
future feature enhancements. Here's a breakdown of its components:

- Master                   : Handles core data and functionalities pivotal for the system's operation.
- Coach Appointment System : Provides specialized functionality for scheduling coaching appointments.

The platform is configured to operate in the UTC+8 timezone. Users can access the platform via the following URLs:

/coach_appointment_booking : Access coach schedules and book coaching appointments.
/coach_appointment_record  : View the history of past appointments.
/admin                     : Manage master data. (Credentials: Username - khleong, Password - 12345678)

====================================================================================================

To set up the environment before launching the web app, use the following Conda command:
conda env create -f environment.yml

Once the environment setup is complete, you can launch the web app using the following Conda commands. Ensure your directory points to the web app:

1. Activate the Conda environment:
   conda activate coach_management_platform

2. Run the Django development server:
   python manage.py runserver