from django import forms 
from .models import DemandeConge

class DemandeCongeForm(forms.ModelForm):
    class Meta:
        model = DemandeConge
        fields = ['nom', 'prenom', 'type_conge', 'date_debut', 'date_fin', 'motif']