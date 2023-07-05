from django.db import models

class DemandeDocteur(models.Model):
    collaboration = models.ForeignKey("Collaboration", on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    specialite = models.ForeignKey("Specialite", on_delete=models.CASCADE, null=True)
    etat = models.IntegerField() #1 accepte

    class Meta:
        db_table = 'demande_docteur'

    def inserer_demande(collaboration,email,password,specialite):
        demande = DemandeDocteur(collaboration=collaboration,email=email,password=password,specialite=specialite,etat=0)
        demande.save()

    def update(demande):
        demande.etat= 1
        demande.save()