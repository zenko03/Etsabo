from django.db import models
import datetime
from datetime import datetime



import random

class EtudeDocteur(models.Model):
    docteur = models.ForeignKey("Medecin",on_delete=models.CASCADE)
    fianarana = models.CharField(max_length=90)
    annee_debut = models.IntegerField()
    annee_fin = models.IntegerField()

    class Meta:
        db_table = 'etude_docteur'




