from django.db import models


class Pharmacie(models.Model):
    nom_pharmacie = models.CharField(max_length=80)
    long =  models.FloatField()
    lat =  models.FloatField()
    
    class Meta:
        db_table = 'pharmacie'

    
