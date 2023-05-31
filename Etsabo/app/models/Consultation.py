from django.db import models


class Consultation(models.Model):
    medecin = models.ForeignKey("Medecin", on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    date_consultation= models.DateField(auto_now=False, auto_now_add=False) 
    symptomes = models.CharField(max_length=500)
    diagnostic = models.CharField(max_length=500)
    
