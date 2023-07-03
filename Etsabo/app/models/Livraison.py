from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from .Patient import Patient


class Livraison(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    datetime_livraison = models.DateTimeField()
    adresse = models.CharField(max_length=90)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    etat = models.IntegerField()

    class Meta:
        db_table = 'livraison'













