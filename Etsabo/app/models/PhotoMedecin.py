from django.db import models


class PhotoMedecin(models.Model):
    medecin = models.ForeignKey("Medecin", on_delete=models.CASCADE, null=True)
    src = models.CharField(max_length=70)

    class Meta:
        db_table = 'photo_medecin'






