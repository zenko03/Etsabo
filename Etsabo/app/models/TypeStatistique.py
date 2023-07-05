from django.db import models


class TypeStatistique(models.Model):
    nom = models.CharField(max_length=60)

    class Meta:
        db_table = 'type_statistique'