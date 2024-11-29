from django.db import models

# Create your models here.
class DemandeConge(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    type_conge = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    motif = models.TextField()
    date_demande = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Demande faite par " + self.nom + " " + self.prenom
        
class Employe(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    date_embauche = models.DateField()
    date_naissance = models.DateField()
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    poste = models.CharField(max_length=50)
    photo_profil = models.CharField(max_length=1000, default="https://www.freepik.com/premium-vector/default-profile-picture-ui-element-template_44646706.htm")
    
    def __str__(self):
        return self.nom + " " + self.prenom
    
    
    class CreateTask(models.Model):
        task = models.CharField(max_length=10000)
        date_created = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
            return self.task