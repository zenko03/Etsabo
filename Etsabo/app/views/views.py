from datetime import datetime
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import redirect
from app.models import Medecin
from app.models import Publicite
from app.models import ConseilsSanitaire
from app.models import Objet
from app.models import Patient
from app.models import Rdv
import sys

def home(request):
    medecins = Medecin.objects.all()
    pubs = Publicite.objects.filter(date_fin__gte=timezone.now())
    random_pubs = Publicite.get_random_Pub(pubs, 2)
    
    objets = Objet.getAllObjet()

    conseil = ConseilsSanitaire.objects.all()[0]
    context = {
        'medecins': medecins,
        'pubs': random_pubs,
        'conseil':conseil,
        'objets':objets
    }
    
    return render(request, 'accueil.html',context)

def boutique(request):

    objets = Objet.getAllObjet()

    context = {
        'objets':objets
    }

    return render(request, 'boutique.html',context)

def listeDiscu(request):
    return render(request, 'Listediscussion.html')

def profilMedecin(request):
    id_medecin = request.GET.get('idMedecin')
    medecin = Medecin.objects.select_related('specialite').get(id=id_medecin)
    etudedocteurs = medecin.etudedocteur_set.all()
    context = {
        'medecin': medecin,
        'etudes': etudedocteurs
    }
    return render(request, 'ProfilDocteur.html', context)

def listeMedecin(request):
    medecins = Medecin.objects.select_related('specialite')
    context = {'medecins': medecins}
    return render(request, 'listeMedecin.html', context)

def listePatient(request):
    patient= Patient.objects.filter(etat=0)
    patients= list(patient)
    context = {'patients': patients}
    return render(request,'listePatient.html',context)

def modifierPatient(request):
    idPatient = request.GET.get('idPatient')
    patient = Patient.objects.get(id=idPatient)
    context = {'patient': patient}
    return render(request, 'modifierPatient.html', context)

def modificationPatient(request):
    idPatient= request.POST.get('idPatient')
    adresse = request.POST.get('adresse')
    tel = request.POST.get('tel')
    ddn= request.POST.get('ddn')
    email= request.POST.get('email')
    patient = Patient.objects.get(id=idPatient)
    print("tel ", tel, file=sys.stdout)
    patient.modifierPatient(adresse,tel,ddn,email)
    return redirect('listePatient')

def recherchePatient(request):
    recherche = request.POST.get('recherche')
    patients= Patient.rechercherPatient(recherche)
    context = {
        'patients': patients
    }
    return render(request, 'recherchePatient.html', context)

def listeMedecinBack(request):
    medecins = Medecin.objects.select_related('specialite')
    context = {'medecins': medecins}
    return render(request,'listeMedecinBack.html',context)

def rdvDispoMedecin(request):
    id_medecin = request.GET.get('idMedecin')
    listRdv = Rdv.objects.select_related('patient').filter(status=0, medecin_id=id_medecin,dateheure_rdv__gte=timezone.now())
    context = {'listeRdv':listRdv}
    return render(request,'rdvDispo.html',context)

def rdvEnCours(request):
    id_medecin = request.GET.get('idMedecin')
    listRdv = Rdv.objects.select_related('patient').filter(status=1, medecin_id=id_medecin, dateheure_rdv__gte=timezone.now())
    context = {'listeRdv': listRdv}
    return render(request, 'rdvEnCours.html', context)

def accepter_rdv(request):
    id_rdv= request.GET.get('idRdv')
    rdv= Rdv.objects.get(id=id_rdv)
    rdv.accepter_rdv()
    return redirect('listeMedecinBack')

def decliner_rdv(request):
    id_rdv = request.GET.get('idRdv')
    rdv = Rdv.objects.get(id=id_rdv)
    rdv.decliner_rdv()
    return redirect('listeMedecinBack')

def terminer_rdv(request):
    id_rdv = request.GET.get('idRdv')
    rdv = Rdv.objects.get(id=id_rdv)
    rdv.terminer_rdv()
    return redirect('listeMedecinBack')