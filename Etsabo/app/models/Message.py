from django.db import models


class Message(models.Model):
    medecin = models.ForeignKey("Medecin", on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    type = models.IntegerField()
    contenus = models.CharField(max_length=500)
    date_envoie = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = 'message'