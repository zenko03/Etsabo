from django.db import models


class Patient(models.Model):
    nom = models.CharField(max_length=30)
    prenoms = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    sexe = models.IntegerField()
    date_de_naissance =models.DateTimeField(null=True, blank=True)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    famille =  models.ForeignKey("Famille", on_delete=models.CASCADE, null=True) #1 si simple
    is_actif = models.IntegerField() #0 si pas abonné et 1 si abonné

    class Meta:
        db_table = 'patient'

    @staticmethod  
    def checkLogin(email, password):
        try:
            patient = Patient.objects.get(email=email, password=password)
            return True
        except Patient.DoesNotExist:
            return False

    @staticmethod
    def getPatient(email,password):
        try:
            patient = Patient.objects.get(email=email, password=password)
            return patient
        except Patient.DoesNotExist:
            return None


        
    