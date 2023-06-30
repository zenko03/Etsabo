from django.db import models


class Patient(models.Model):
    nom = models.CharField(max_length=30)
    prenoms = models.CharField(max_length=30)
    sexe = models.IntegerField() # 0 homme 1 femme
    adresse = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    date_de_naissance =models.DateTimeField(null=True, blank=True)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    famille =  models.ForeignKey("Famille", on_delete=models.CASCADE) #1 si simple
    is_actif = models.IntegerField() #0 si pas abonné et 1 si abonné
    etat = models.IntegerField() #1 ra efa supprimé

    class Meta:
        db_table = 'patient'

    def modifierPatient(patient,adresse,telephone,ddn,email):
        patient.adresse=adresse
        patient.telephone=telephone
        patient.date_de_naissance=ddn
        patient.email=email
        patient.save()

    def supprimerPatient(idPatient):
        patient = Patient.objects.get(id=idPatient)
        patient.etat=1
        patient.save()

    def rechercherPatient(mot):
        patient = Patient.objects.filter(nom__icontains=mot) | Patient.objects.filter(prenoms__icontains=mot)
        patients= list(patient)
        return patients

    