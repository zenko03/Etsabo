from datetime import datetime
from models import Abonnement
from django.db import models
from datetime import timedelta
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

class Patient(models.Model):
    nom = models.CharField(max_length=30)
    prenoms = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    date_de_naissance = models.CharField(max_length=20)
    email = models.EmailField(default="",unique=True)
    password = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "Patient"

    def __init__(self, nom, prenoms, adresse, telephone, date_de_naissance, email, password, *args, **kwargs):
        super(Patient, self).__init__(*args, **kwargs)
        self.nom = nom
        self.prenoms = prenoms
        self.adresse = adresse
        self.telephone = telephone
        self.date_de_naissance = date_de_naissance
        self.email = email
        self.password = password

    @classmethod
    def inscrire(cls, nom, prenoms, adresse, telephone, date_de_naissance, email, password):
        patient = cls(nom=nom, prenoms=prenoms, adresse=adresse, telephone=telephone, date_de_naissance=date_de_naissance, email=email, password=make_password(password))
        patient.save()
        return patient

    @classmethod
    def login(cls, email, password):
        try:
            patient = cls.objects.get(email=email)
            if check_password(password, patient.password):
                return patient
        except cls.DoesNotExist:
            pass
        return None

    @classmethod
    def get_patient_by_id(cls, patient_id):
        try:
            patient = cls.objects.get(id=patient_id)
            return patient
        except cls.DoesNotExist:
            return None

    @classmethod
    def do_abonnement(cls, patient_id, type_id, reference):
        try:
            patient = cls.objects.get(id=patient_id)
            date_actuelle = datetime.now()
            date_dans_30_jours = date_actuelle + timedelta(days=30)
            Abonnement.insert(patient_id,date_dans_30_jours,reference,type_id)
        except cls.DoesNotExist:
            return None


        