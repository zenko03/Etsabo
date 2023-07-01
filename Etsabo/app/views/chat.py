from django.shortcuts import render, redirect, HttpResponse
from .. import models
from json import dumps, loads
from django.core import serializers
from django.http import JsonResponse


def chat(request : HttpResponse):
    return render(request, 'chat.html')

def get_current_conversation(request : HttpResponse):
    est_patient = request.GET.get('est_patient')
    patient_id = request.GET.get('patient')
    medecin_id = request.GET.get('medecin')

    conversation = serializers.serialize("json", models.Message.get_messages_from(patient_id, medecin_id))
    conversation_json = loads(conversation)

    # return HttpResponse(dumps(conversation_json), content_type='application/json')
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == "GET":
            return JsonResponse(conversation_json, safe=False)

def envoyer_message(request : HttpResponse):
    est_patient = request.GET.get('est_patient')
    patient_id = request.GET.get('patient')
    medecin_id = request.GET.get('medecin')
    message = request.GET.get('message')

    models.Message.send_message_to(patient_id, medecin_id, message, True if est_patient == 0 else False)

    return HttpResponse(f"Send Patient: {patient_id} | Medecin: {medecin_id} | Message: {message}")