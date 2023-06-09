from django.db import models
from datetime import datetime
from .. import models as model


class Message(models.Model):
    medecin = models.ForeignKey("Medecin", on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    type = models.IntegerField()
    contenus = models.CharField(max_length=500)
    date_envoie = models.DateField(auto_now=True)

    class Meta:
        db_table = "Message"

    @staticmethod
    def get_messages_from(patient : int, medecin : int):
        messages = Message.objects.filter(patient = patient, medecin = medecin).order_by("date_envoie")
        return list(messages)

    @staticmethod
    def send_message_to(sender : int, receiver : int, message_str : str, est_patient : bool):
        message : Message = Message()
        message.contenus = message_str
        message.type = 1 if not est_patient else 0
        message.patient = model.Patient.objects.get(pk=sender)
        message.medecin = model.Medecin.objects.get(pk=receiver)

        
        message.save()
    
    @staticmethod
    def get_last_message_from(patient : int, medecin : int):
        last_message = Message.objects.filter(models.Q(medecin__exact = medecin) & models.Q(patient__exact = patient)).order_by("-date_envoie").first()

        return last_message
        
