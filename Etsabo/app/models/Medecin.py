from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from .Specialite import Specialite

class Medecin(models.Model):
    nom = models.CharField(max_length=30)
    prenoms = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    specialite = models.ForeignKey("Specialite", on_delete=models.CASCADE, null=True)
    

    class Meta:
        db_table = 'medecin'

    def set_nom(self,nom):
        self.nom = nom

    def set_prenoms(self,prenoms):
        self.prenoms = prenoms

    def set_email(self,email):
        self.email = email

    def set_password(self,password):
        self.password = password

    def set_specialite(self,specialite):
        self.specialite = specialite

    @staticmethod
    def getAll():
        return Medecin.objects.all()

    @staticmethod
    def create(nom, prenoms, email, password, specialite):
        medecin = Medecin()
        medecin.set_nom(nom)
        medecin.set_prenoms(prenoms)
        medecin.set_email(email)
        medecin.set_password(password)
        medecin.set_specialite(nom)
        medecin.clean_fields()
        try:
            medecin.save()
        except IntegrityError:
            raise ValidationError("Le medecin " + str(nom) + " " + str(prenoms) + " existe déjà")
        return medecin

    def update(self, nom, prenoms, email, password, specialite):
        self.set_nom(nom)
        self.set_prenoms(prenoms)
        self.set_email(email)
        self.set_password(password)
        self.set_specialite(nom)
        self.clean_fields()
        try:
            self.save()
        except IntegrityError:
            raise ValidationError("Le medecin " + str(nom) + " " + str(prenoms) + " existe déjà")
        return self

    def remove(self):
        self.delete()
        return 0









