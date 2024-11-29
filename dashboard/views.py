from django.shortcuts import render
from .

# Create your views here.

def admin_dashboard(request):
    context = {
        "admin" : "Administrator"
        }
    return render(request, 'admin_dashboard.html', context=context)

def home(request):

    return render(request, 'homepage.html')