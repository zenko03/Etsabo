from django.db import models
from django.utils import timezone
from datetime import timedelta

class Collaboration(models.Model):
    nom = models.CharField( max_length=20)
    prenoms = models.CharField(max_length=20)
    fonction = models.ForeignKey("FonctionCollab", on_delete=models.CASCADE)
    biographie = models.CharField(max_length=500)
    piece_jointe = models.CharField(max_length=500)
    date_demande = models.DateTimeField( auto_now=False, auto_now_add=False)
    date_fin = models.DateTimeField( auto_now=False, auto_now_add=False, null=True)
    etat = models.IntegerField() # 1 accepté 0 demande -1 annulé

    class Meta:
        db_table = 'collaboration'

    def inserer_collaborateur(nom,prenoms,fonction,biographie,fichier):
        collaboration = Collaboration(nom=nom,prenoms=prenoms,fonction=fonction,biographie=biographie,piece_jointe=fichier,date_demande=timezone.now(),date_fin=None,etat=0)
        collaboration.save()

    def accepter_collaboration(collab,fonction):
        collab.etat=1
        collab.date_demande = timezone.now()
        collab.date_fin= collab.date_demande + timedelta(weeks=fonction.temps)
        collab.save()

    def refuser_collaboration(collab):
        collab.etat=-1
        collab.save()