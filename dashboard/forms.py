from django import forms 
from .models import DemandeConge, CreateTask

class DemandeCongeForm(forms.ModelForm):
    class Meta:
        model = DemandeConge
        fields = ['nom', 'prenom', 'type_conge', 'date_debut', 'date_fin', 'motif']

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = CreateTask
        fields = ['task_name', 'task_description']