from django.shortcuts import render


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