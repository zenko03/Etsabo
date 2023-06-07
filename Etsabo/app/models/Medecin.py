from django.db import models


class Medecin(models.Model):
    nom = models.CharField(max_length=30)
    prenoms = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    specialite = models.ForeignKey("Specialite", on_delete=models.CASCADE)
