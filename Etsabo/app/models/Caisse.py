from django.db import models

class Caisse(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    montant = models.FloatField()

    class Meta:
        db_table = 'caisse'