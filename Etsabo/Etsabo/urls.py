"""Etsabo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import views as v
from app.views import chat as chat
from app.views import localisation as localisation

urlpatterns = [
    path('', v.home,name='home'),
    path('boutique/',v.boutique,name='boutique'),
    path('listeDiscu/',v.listeDiscu,name='listeDiscu'),
    path('profilMedecin/',v.profilMedecin,name='profilMedecin'),
    path('listeMedecin/',v.listeMedecin,name='listeMedecin'),
    path('listePatient/',v.listePatient,name='listePatient'),
    path('modifierPatient/',v.modifierPatient,name='modifierPatient'),
    path('modificationPatient/',v.modificationPatient,name='modificationPatient'),
    path('recherchePatient/',v.recherchePatient,name='recherchePatient'),
    path('listeMedecinBack/',v.listeMedecinBack,name='listeMedecinBack'),
    path('rdvDispoMedecin/',v.rdvDispoMedecin,name='rdvDispoMedecin'),
    path('rdvEnCours/',v.rdvEnCours,name='rdvEnCours'),
    path('accepter_rdv/',v.accepter_rdv,name='accepter_rdv'),
    path('decliner_rdv/',v.decliner_rdv,name='decliner_rdv'),
    path('terminer_rdv/',v.terminer_rdv,name='terminer_rdv'),
    path('collaboration/',v.collaboration,name='collaboration'),
    path('inserer_collab/',v.inserer_collab,name='inserer_collab'),
    path('collabBack/',v.collabBack,name='collabBack'),
    path('demande_collab/',v.demande_collab,name='demande_collab'),
    path('collab_EnCours/',v.collab_EnCours,name='collab_EnCours'),
    path('accepter_collab/',v.accepter_collab,name='accepter_collab'),
    path('refuser_collab/',v.refuser_collab,name='refuser_collab'),
    path('chat/', chat.chat, name='chat'),
    path('chat/conversation/', chat.get_current_conversation, name='conversation'),
    path('chat/send/', chat.envoyer_message, name='send'),
    path('localisation/pharmacie/', localisation.pharmacie, name='localisation_pharmacie')
]
