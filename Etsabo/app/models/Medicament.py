from django.db import models


class Medicament(models.Model):
    nom = models.CharField( max_length=20)
    
