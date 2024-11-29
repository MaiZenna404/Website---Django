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