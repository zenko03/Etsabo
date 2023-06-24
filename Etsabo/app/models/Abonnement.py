from django.db import models


class Abonnement(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    date_fin = models.DateTimeField(null=True, blank=True)
    type = models.ForeignKey("TypeAbonnement", on_delete=models.CASCADE)

    class Meta:
        db_table = 'abonnement'

    
