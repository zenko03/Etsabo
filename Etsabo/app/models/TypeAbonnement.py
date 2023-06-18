from django.db import models


class TypeAbonnement(models.Model):
    nom_abonnement = models.CharField(max_length=70)
    prix =  models.FloatField()
    
    class Meta:
        db_table = 'type_abonnement'

    
