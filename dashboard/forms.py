from django import forms 
from .models import DemandeConge, CreateTask

class DemandeCongeForm(forms.ModelForm):
    class Meta:
        model = DemandeConge
        fields = ['nom', 'prenom', 'type_conge', 'date_debut', 'date_fin', 'motif']
        widgets = { # Pour passer les classes Tailwind CSS aux champs de formulaire
            'nom': forms.TextInput(attrs={'class': 'w-full m-2 p-5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'prenom': forms.TextInput(attrs={'class': 'w-full m-2 p-5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'type_conge': forms.Select(attrs={'class': 'w-full m-2 p-5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'date_debut': forms.DateInput(attrs={'class': 'w-full m-2 p-5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'w-full m-2 p-5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'type': 'date'}),
            'motif': forms.Textarea(attrs={'class': 'w-full m-2 p-5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = CreateTask
        fields = ['task_name', 'task_description']
        widgets = { # Pour passer les classes Tailwind CSS aux champs de formulaire
            'task_name': forms.TextInput(attrs={'class': 'w-full m-2 p-5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'task_description': forms.TextInput(attrs={'class': 'w-full m-2 p-5 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})
            }