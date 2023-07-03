from django.db import models


class Rdv(models.Model):
    medecin = models.ForeignKey("Medecin", on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    dateheure_rdv = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.IntegerField()  # 0: soumis  1: accepté  2: terminé  -1: annulé

    class Meta:
        db_table = 'rdv'