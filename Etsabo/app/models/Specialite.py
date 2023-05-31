from django.db import models


class Specialite(models.Model):
    nom = models.CharField(max_length=20)


     