from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
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

    def set_titre(self,titre):
        self.titre = titre

    def set_description(self,description):
        self.description = description

    def set_photo(self,photo):
        self.photo = photo

    def set_debut(self,debut):
        self.date_debut = debut

    def set_fin(self,fin):
        self.date_fin = fin

    def get_random_Pub(pubs, num):
        
        pubs_list = list(pubs)  # Convertir les objets Publicite en liste
        if num >= len(pubs_list):
            return pubs_list
        else:
            random_pubs = random.sample(pubs_list, num)
            return random_pubs

    @staticmethod
    def getAll():
        return Publicite.objects.all()

    @staticmethod
    def create(titre, description, photo, debut, fin):
        publicite = Publicite()
        publicite.set_titre(titre)
        publicite.set_description(description)
        publicite.set_photo(photo)
        publicite.set_debut(debut)
        publicite.set_fin(fin)
        publicite.clean_fields()
        try:
            publicite.save()
        except IntegrityError:
            raise ValidationError("La publicite " + str(titre) + " existe déjà")
        return publicite

    def update(self, titre, description, photo, debut, fin):
        self.set_titre(titre)
        self.set_description(description)
        self.set_photo(photo)
        self.set_debut(debut)
        self.set_fin(fin)
        self.clean_fields()
        try:
            self.save()
        except IntegrityError:
            raise ValidationError("La publicite " + str(titre) + " existe déjà")
        return self

    def remove(self):
        self.delete()
        return 0
