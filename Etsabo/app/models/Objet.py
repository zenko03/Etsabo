from django.db import models


class Objet(models.Model):
    nom_objet = models.CharField(max_length=70)
    prix = models.FloatField()
    
    class Meta:
        db_table = 'objet'

    
