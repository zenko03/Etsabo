from django.db import models


class Ordonnance(models.Model):
    consultation = models.ForeignKey("Consultation", on_delete=models.CASCADE)  
    medocs = models.CharField(max_length=200)
    prise = models.CharField(max_length=20)
    remarque = models.CharField(max_length=200)

    class Meta:
        db_table = 'ordonnance'