from django.db import models


class Medecin(models.Model):
    nom = models.CharField(max_length=30)
    prenoms = models.CharField(max_length=30)
    email = models.EmailField(default="")
    specialite = models.ForeignKey("Specialite", on_delete=models.CASCADE)

    class Meta:
        db_table = "Medecin"

    def __init__(self, nom, prenoms, email, specialite, *args, **kwargs):
        super(Medecin, self).__init__(*args, **kwargs)
        self.nom = nom
        self.prenoms = prenoms
        self.email = email
        self.specialite = specialite

    @classmethod
    def get_by_id(cls, medecin_id):
        try:
            medecin = cls.objects.get(id=medecin_id)
            return medecin
        except cls.DoesNotExist:
            return None
