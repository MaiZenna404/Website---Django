from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def admin_dashboard(request):
    context = {
        "admin" : "Administrator"
        }
    return render(request, 'admin_dashboard.html', context=context)

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
    return render(request, 'employee_dashboard.html', context=context)

def view_employees(request):
    employees = Employe.objects.all()
    context = {
        'employees': employees,
        'admin': "Administrator",
        "total_employees": len(employees)
    }
    return render(request, 'view_employees.html', context=context)

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
    return render(request, 'admin_create_task.html', context=context)

def view_tasks(request):
    tasks = ViewTask.objects.all()
    context = {
        'tasks': tasks,
        'admin': "Administrator",
        "total_tasks": len(tasks)
    }
    return render(request, 'admin_view_task.html', context=context)