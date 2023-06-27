from django.db import models


class Objet(models.Model):
    nom_objet = models.CharField(max_length=70)
    prix = models.FloatField()
    
    class Meta:
        db_table = 'objet'

    @staticmethod
    def getAllObjet():
        return Objet.objects.all().prefetch_related('photoobjet_set')

 
