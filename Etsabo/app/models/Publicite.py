from django.db import models
import datetime
from datetime import datetime



import random

class Publicite(models.Model):
    titre = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    photo = models.CharField(max_length=30)
    date_debut = models.DateTimeField(null=True)
    date_fin = models.DateTimeField(null=True)

    class Meta:
        db_table = 'publicite'

    def get_random_Pub(pubs, num):
        
        pubs_list = list(pubs)  # Convertir les objets Publicite en liste
        if num >= len(pubs_list):
            return pubs_list
        else:
            random_pubs = random.sample(pubs_list, num)
            return random_pubs


