from django.db import models


class Abonnement(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    date_fin = models.DateTimeField(null=True, blank=True)
    reference = models.CharField(max_length=15)
    type = models.ForeignKey("TypeAbonnement", on_delete=models.CASCADE)

    class Meta:
        db_table = 'abonnement'

    def __init__(self, patient, date_fin, reference, type, *args, **kwargs):
        super(Abonnement, self).__init__(*args, **kwargs)
        self.patient = patient
        self.date_fin = date_fin
        self.reference = reference
        self.type = type

    @classmethod
    def insert(cls,patient,date_fin,reference,type):
        abonnement = cls(patient=patient,date_fin=date_fin,reference=reference,type=type)
        abonnement.save()
        return abonnement

    
