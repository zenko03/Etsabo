from django.db import models
from datetime import datetime
from . import *


class Message(models.Model):
    medecin = models.ForeignKey("Medecin", on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    type = models.IntegerField()
    contenus = models.CharField(max_length=500)
    date_envoie = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = "Message"

    @staticmethod
    def get_messages_from(patient : int, medecin : int):
        messages = Message.objects.filter(patient = patient, medecin = medecin).order_by("date_envoie")
        return messages

    def send_message_to(self, sender : int, message : str, est_patient : bool):
        message : Message = Message()
        message.contenus = message
        message.type = 1 if not est_patient else 0
        if est_patient:
            message.patient = sender
        else:
            message.medecin = sender
        
        message.save()
        
