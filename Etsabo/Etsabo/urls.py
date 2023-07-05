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
    path('',v.login,name='login'),
    path('choice/',v.choice,name='choice'),
    path('profil/',v.profil,name='profil'),
    path('deconnecter/',v.deconnexion,name='deconnecter'),
    path('next-choice/',v.account_choice,name='next-choice'),
    path('inscriFamille/', v.inscription_famille, name='inscription-famille'),
    path('inscriPerso/', v.inscription_perso, name='inscription-perso'),
    path('Checklogin/',v.checkLogin,name='Checklogin'),
    path('home/', v.home,name='home'),
    path('boutique/',v.boutique,name='boutique'),
    path('listeDiscu/',v.listeDiscu,name='listeDiscu'),
    path('panier/',v.panier,name='panier'),
    path('viderPanier/',v.viderPanier,name='viderPanier'),
    path('chat/', chat.chat, name='chat'),
    path('chat/conversation/', chat.get_current_conversation, name='conversation'),
    path('chat/send/', chat.envoyer_message, name='send'),
    path('localisation/pharmacie/', localisation.pharmacie, name='localisation_pharmacie'),
    path('ajouter-au-panier/<int:objet_id>/', v.ajouter_au_panier, name='ajouter_au_panier'),
    path('suppr/<int:objet_id>/', v.supprimer, name='suppr'),
    path('profilMedecin/',v.profilMedecin,name='profilMedecin'),
    path('listeMedecin/',v.listeMedecin,name='listeMedecin'),
    path('famille/', v.familleV, name='famille'),
    path('ajouter-membre/', v.ajouter_membre, name='ajouter-membre'),
    path('livraison/',v.livraison,name='livraison'),
    path('ajouter_livraison/', v.ajouter_livraison, name='ajouter_livraison'),
    path('abonnement/',v.abonnement,name='abonnement'),
    path('addAbonnement/',v.ajouter_abonnement,name='addAbonnement'),
    path('modifierPatient/', v.modifierPatient, name='modifierPatient'),
    path('modificationPatient/', v.modificationPatient, name='modificationPatient'),
    path('collaboration/',v.collaboration,name='collaboration'),
    path('inserer_collab/',v.inserer_collab,name='inserer_collab'),
    path('inserer_docteur/',v.inserer_docteur,name='inserer_docteur'),
    path('collabBack/', v.collabBack, name='collabBack'),
    path('demande_collab/', v.demande_collab, name='demande_collab'),
    path('collab_EnCours/', v.collab_EnCours, name='collab_EnCours'),
    path('accepter_collab/', v.accepter_collab, name='accepter_collab'),
    path('refuser_collab/', v.refuser_collab, name='refuser_collab'),

    #-----------------Docteur back office
    path('baseDocteur/',v.homeDocteur,name='baseDocteur'),
    path('ordonnance/', v.ordonnance, name='ordonnance'),
    path('get_patient_suggestions/', v.get_patient_suggestions, name='get_patient_suggestions'),
    path('loginDocteur/', v.loginDocteur, name='loginDocteur'),
    path('checkDocteur/',v.checkLoginDoc,name='checkLoginDoc'),
    path('create_consultation/',v.create_consultation,name='create_consultation')


]

