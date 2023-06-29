from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


class Medecin(models.Model):
    nom = models.CharField(max_length=30)
    prenoms = models.CharField(max_length=30)
    email = models.EmailField(default="",unique=True)
    password = models.CharField(max_length=30,default="")
    specialite = models.ForeignKey("Specialite", on_delete=models.CASCADE)

    class Meta:
        db_table = "Medecin"

    def __init__(self, nom, prenoms, email, password, specialite, *args, **kwargs):
        super(Medecin, self).__init__(*args, **kwargs)
        self.nom = nom
        self.prenoms = prenoms
        self.email = email
        self.password = password
        self.specialite = specialite

    @classmethod
    def inscription(cls, nom, prenoms, email, password, specialite):
        medecin = cls(nom=nom, prenoms=prenoms, email=email, password=make_password(password), specialite=specialite)
        medecin.save()
        return medecin

    @classmethod
    def login(cls, email, password):
        try:
            medecin = cls.objects.get(email=email)
            if check_password(password, medecin.password):
                return medecin
        except cls.DoesNotExist:
            pass
        return None

    @classmethod
    def get_by_id(cls, medecin_id):
        try:
            medecin = cls.objects.get(id=medecin_id)
            return medecin
        except cls.DoesNotExist:
            return None
