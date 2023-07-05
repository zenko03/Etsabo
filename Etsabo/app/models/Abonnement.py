from datetime import datetime
from django.utils import timezone

from django.db import models
from django.utils.timezone import now

from app.models import Patient


class Abonnement(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    date_fin = models.DateTimeField(null=True, blank=True)
    type = models.ForeignKey("TypeAbonnement", on_delete=models.CASCADE)
    reference = models.CharField(max_length=15)

    class Meta:
        db_table = 'abonnement'

    from datetime import datetime

    @staticmethod
    def estAbonner(patient):
        current_datetime = datetime.now()
        latest_subscription = Abonnement.get_latest_subscription(patient)
        if latest_subscription and latest_subscription.date_fin and latest_subscription.date_fin > current_datetime:
            return True
        else:
            return False
    @staticmethod
    def get_latest_subscription(patient):
        try:
            latest_subscription = Abonnement.objects.filter(patient=patient).latest('date_fin')
            return latest_subscription
        except Abonnement.DoesNotExist:
            return None

    @staticmethod
    def verifierAbonnement():
        current_datetime = timezone.localtime()
        patients = Patient.objects.all()
        for patient in patients:
            latest_subscription = Abonnement.get_latest_subscription(patient)
            if not latest_subscription:
                patient.is_actif = 0
                patient.save(update_fields=['is_actif'])
            if latest_subscription and latest_subscription.date_fin and latest_subscription.date_fin <= current_datetime:
                patient.is_actif = 0
                patient.save(update_fields=['is_actif'])

    from django.utils import timezone
    @staticmethod
    def getAbonnementEncours():
        abonnements_en_cours = Abonnement.objects.filter(patient__is_actif=0).select_related('patient', 'type')
        allAb = []
        for ab in abonnements_en_cours:
            if ab.patient.is_actif==0:
                allAb.append(ab)


        return allAb



