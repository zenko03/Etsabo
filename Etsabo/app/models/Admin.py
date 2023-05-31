from django.db import models


class Admin(models.Model):
    nom = models.CharField(max_length=30)
    email = models.CharField(max_length=40)

