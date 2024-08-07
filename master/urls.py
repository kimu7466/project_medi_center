from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard_view/', dashboard_view, name='dashboard_view'),
    path('doctors_view/', doctors_view, name='doctors_view'),
    path('add_doctors_view/', add_doctors_view, name='add_doctors_view'),
    path('edit_doctors_view/<int:doctor_id>', edit_doctors_view, name='edit_doctors_view'),
    path('delete_doctors_view/<int:doctor_id>', delete_doctors_view, name='delete_doctors_view'),
    path('patients_view/', patients_view, name='patients_view'),
    path('tasks_view/', tasks_view, name='tasks_view'),
    path('patient_delete/<int:patient_id>', patient_delete, name='patient_delete'),
    path('patient_update/<int:patient_id>', patient_update, name='patient_update'),
    path('patient_account/<int:patient_id>', patient_account, name='patient_account'),
]
