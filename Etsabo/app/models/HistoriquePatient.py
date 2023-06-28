from django.db import models

class HistoriquePatient(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    date_modif = models.DateTimeField(null=True)
    admin = models.ForeignKey("Admin", on_delete=models.CASCADE)

    class Meta:
        db_table = 'historiquePatient'

