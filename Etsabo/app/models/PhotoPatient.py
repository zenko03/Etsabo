from django.db import models


class PhotoPatient(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE, null=True)
    src = models.CharField(max_length=70)

    class Meta:
        db_table = 'photo_patient'






