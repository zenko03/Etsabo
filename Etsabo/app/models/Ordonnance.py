from django.db import models


class Ordonnance(models.Model):
    consultation = models.ForeignKey("Consultation", on_delete=models.CASCADE)  
    medocs = models.ForeignKey("Medicament", on_delete=models.CASCADE)
    prise = models.CharField(max_length=20)

    class Meta:
        db_table = 'ordonnance'