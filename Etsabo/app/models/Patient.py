from django.db import models


class Patient(models.Model):
    nom = models.CharField(max_length=30)
    prenoms = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    date_de_naissance = models.CharField(max_length=20)
    