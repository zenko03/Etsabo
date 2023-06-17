from django.db import models


class Rdv(models.Model):
    medecin = models.ForeignKey("Medecin", on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    date_rdv = models.DateField( auto_now=False, auto_now_add=False)
    heure_rdv = models.DateTimeField( auto_now=False, auto_now_add=False)
    status = models.IntegerField

    class Meta:
        db_table = 'rdv'