from django.shortcuts import render
from django.utils.timezone import now
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.


def my_view(request):
    response = render(request, 'my_template.html')
    # Désactivation du cache pour éviter les 304
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def admin_dashboard(request):
    context = {
        "admin" : "Administrator",
        'timestamp': now().timestamp()
        }
    response = render(request, 'admin_dashboard.html', context)
    # Disable caching to avoid 304 responses
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def home(request):

    return render(request, 'homepage.html')

def employee_dashboard(request):
    if request.method == 'POST':
        form = DemandeCongeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Votre demande a bien été enregistrée")
    else:
        form = DemandeCongeForm()
    
    context = {
        "employe": "Employe",
        "form": form
    }
    response = render(request, 'employee_dashboard.html', context)
    # Disable caching to avoid 304 responses
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def view_employees(request):
    employees = Employe.objects.all()
    context = {
        'employees': employees,
        'admin': "Administrator",
        "total_employees": len(employees)
    }
    response = render(request, 'view_employees.html', context)
    # Disable caching to avoid 304 responses
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            return HttpResponse("Votre tâche a bien été enregistrée !")
    else:
        form = CreateTaskForm()
    context = {
        'admin': "Administrator",
        "form": form
    }
    response = render(request, 'admin_create_task.html', context)
    # Disable caching to avoid 304 responses
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def view_tasks(request):
    tasks = ViewTask.objects.all()
    context = {
        'tasks': tasks,
        'admin': "Administrator",
        "total_tasks": len(tasks)
    }
    response = render(request, 'admin_view_task.html', context)
    # Disable caching to avoid 304 responses
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def show_demande_conges(request):
    demandes = DemandeConge.objects.all()
    context = {
        'demande': demandes,
        'admin': "Administrator",
        "total_demande": len(demandes)
    }
    response = render(request, 'admin_dashboard.html', context)
    # Disable caching to avoid 304 responses
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
