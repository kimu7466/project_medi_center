from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'dashboard.html')
def doctors_view(request):
    return render(request, 'doctors.html')
def patients_view(request):
    return render(request, 'patients.html')
def names_view(request):
    return render(request, 'names.html')
def feedback_view(request):
    return render (request, 'feedback.html')
def p_feedback_view(request):
    return render (request, 'patients_feedback.html')
def p_names_view(request):
    return render (request, 'patients_names.html')
def contacts_view(request):
    return render (request, 'contacts.html')
def help_view(request):
    return render (request, 'help.html')