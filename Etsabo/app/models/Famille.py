from django.db import models


class Famille(models.Model):
    nom_famille = models.CharField(max_length=60)
    adresse = models.CharField(max_length=80)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'famille'

    @staticmethod
    def checkLogin(email, password):
        try:
            famille = Famille.objects.get(email=email, password=password)
            return True
        except Famille.DoesNotExist:
            return False

    @staticmethod
    def getFamille(email, password):
        try:
            famille = Famille.objects.get(email=email, password=password)
            return famille
        except Famille.DoesNotExist:
            return None
