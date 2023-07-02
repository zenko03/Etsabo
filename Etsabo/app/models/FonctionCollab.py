from django.db import models

class FonctionCollab(models.Model):
    type = models.CharField( max_length=20)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    temps = models.IntegerField()

    class Meta:
        db_table = 'fonction'