from django.db import models
from .Livraison import Livraison
from .Objet import Objet

class ObjetALivrer(models.Model):
    livraison = models.ForeignKey(Livraison, on_delete=models.CASCADE)
    objet = models.ForeignKey(Objet,on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'objet_a_livrer'
