from django.db import models

# Create your models here.
class DemandeConge(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    type_congee = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    motif = models.TextField()
    date_demande = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Demande faite par " + self.nom + " " + self.prenom
        