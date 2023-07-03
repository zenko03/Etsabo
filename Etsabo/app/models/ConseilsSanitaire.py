from django.db import models
import datetime
from datetime import datetime



import random

class ConseilsSanitaire(models.Model):
    titre = models.CharField(max_length=90)
    description = models.TextField(max_length=255)
    img = models.CharField(max_length=90)

    class Meta:
        db_table = 'conseils_sanitaire'



