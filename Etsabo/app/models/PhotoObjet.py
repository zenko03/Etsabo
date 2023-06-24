from django.db import models


class PhotoObjet(models.Model):
    objet = models.ForeignKey("Objet", on_delete=models.CASCADE)
    src = models.CharField(max_length=70)
    
    class Meta:
        db_table = 'photo_objet'

    
    
