from django.contrib import admin
from .models import DemandeConge, Employe, CreateTask
# Register your models here.
admin.site.register(DemandeConge)
admin.site.register(Employe)
admin.site.register(CreateTask)