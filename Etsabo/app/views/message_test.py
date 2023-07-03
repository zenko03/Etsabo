from django.shortcuts import render, redirect, HttpResponse
from models import Message
from json import dump

def chat(request : HttpResponse):
    patient = request.get('patient')
    medecin = request.get('medecin')
    est_patient = request.get('est_patient')

    # Obtenir tout les messages
    messages = Message.get_messages_from(medecin=medecin, patient=patient)

    # Mettre contexte
    context = {
        'messages': messages,
        'est_patient': est_patient
    }

    return render(request, "message_test.html", context)