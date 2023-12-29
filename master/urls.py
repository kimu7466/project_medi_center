from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard_view, name='dashboard_view'),
    path('doctors_view/', doctors_view, name='doctors_view'),
    path('patients_view/', patients_view, name='patients_view'),
    path('names_view/', names_view, name='names_view'),
    path('feedback_view/', feedback_view, name='feedback_view'),
    path('p_names_view/', p_names_view, name='p_names_view'),
    path('p_feedback_view/', p_feedback_view, name='p_feedback_view'),
    path('contacts_view/', contacts_view, name='contacts_view'),
    path('help_view/', help_view, name='help_view'),
]