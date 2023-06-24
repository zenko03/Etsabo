from django.db import models


class Famille(models.Model):
    nom_famille = models.CharField(max_length=60)
    adresse = models.CharField(max_length=80)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=60)

    class Meta:
        db_table = 'famille'
    
