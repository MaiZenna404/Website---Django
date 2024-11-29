from django.shortcuts import render
from django.http import HttpResponse
from .forms import DemandeCongeForm

# Create your views here.

def admin_dashboard(request):
    context = {
        "admin" : "Administrator"
        }
    return render(request, 'admin_dashboard.html', context=context)

def home(request):

    return render(request, 'homepage.html')

def employe_dashboard(request):
    context = {
        "employe" : "Employe"
        }
    return render(request, 'employe_dashboard.html', context=context)

def employee_form(request):
    if request.method == 'POST':
        form = DemandeCongeForm(request.POST)
        if form.is_valid():
             return HttpResponse("Votre demande a bien été enregistrée")
    else:
        form = DemandeCongeForm()
        context = {
            "form" : form
        }
    return render(request, 'employe_dashboard.html', context=context)