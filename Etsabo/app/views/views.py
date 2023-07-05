import json
from datetime import datetime, timedelta, timezone
from django.utils import timezone
from django.shortcuts import render
from app.models import Medecin, Livraison, ObjetALivrer, Consultation, Ordonnance
from app.models import Publicite
from app.models import ConseilsSanitaire
from app.models import Objet
from app.models import Famille
from app.models import Patient
from app.models import PhotoPatient
from app.models import TypeAbonnement
from app.models import Abonnement
from django.contrib.sessions.models import Session
from app.models import Collaboration
from app.models import FonctionCollab
from app.models import Specialite
from app.models import DemandeDocteur


def home(request):
    medecins = Medecin.objects.all()
    pubs= Publicite.objects.filter(date_fin__gte=timezone.now())
    random_pubs = Publicite.get_random_Pub(pubs, 2)

    objets = Objet.getAllObjet()

    conseils = ConseilsSanitaire.objects.all() 
    conseil = conseils[0] if len(conseils) > 0 else None
    context = {
        'medecins': medecins,
        'pubs': random_pubs,
        'conseil': conseil,
        'objets': objets
    }

    return render(request, 'accueil.html', context)
#Login et inscription

def login(request):
    Abonnement.verifierAbonnement()
    return render(request,'login.html')

def choice(request):
    return render(request,'choice.html')


# Views.py
def profil(request):
    if 'idSession' in request.session:
        p = Patient.objects.get(id=request.session['idSession'])
        ab = Abonnement.get_latest_subscription(p)
        typeAb = TypeAbonnement.objects.get(id=ab.type.id)
        photo_patient = PhotoPatient.objects.filter(patient=p).first()
        context = {
            'patient': p,
            'photo_patient': photo_patient,
            'abonnement' :ab,
            'typeAb':typeAb
        }
        return render(request, 'profil.html', context)
    else:
        return render(request, 'login.html')

# Views.py
def deconnexion(request):
    if 'idSession' in request.session:
        del request.session['idSession']
    elif 'idFamille' in request.session:
        del request.session['idFamille']
    return render(request, 'login.html')

def account_choice(request):
    if request.method == 'POST':
        account_type = request.POST.get('account-type')

    print(account_type)   
    if(account_type=="0"):
        print("ato pr1")  
        return render(request, 'inscription.html')
    elif(account_type=="10"):
        print("ato pr")  
        return render(request, 'inscriFamille.html')
    else:
        return render(request, 'login.html')

def inscription_famille(request):
    if request.method == 'POST':
        nom_famille = request.POST.get('nom_famille')
        adresse = request.POST.get('adresse')
        email = request.POST.get('email')
        password = request.POST.get('password')

        famille = Famille(nom_famille=nom_famille, adresse=adresse, email=email, password=password)
        famille.save()

        return render(request,'login.html')
    
    return render(request, 'inscriFamille.html')

# Views.py
def inscription_perso(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenoms')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')
        sexe = request.POST.get('sexe')
        dtn = request.POST.get('date_de_naissance')
        email = request.POST.get('email')
        password = request.POST.get('password')

        patient = Patient(nom=nom, prenoms=prenom, adresse=adresse, telephone=telephone, sexe=sexe,
                          date_de_naissance=dtn, email=email, password=password, is_actif=0, famille_id=1)
        patient.save()

        if 'profile_picture' in request.FILES:
            profile_picture = request.FILES['profile_picture']
            filename = str(patient.id) + '.' + profile_picture.name.split('.')[-1]  # Nouveau nom de fichier
            photo_patient = PhotoPatient(patient=patient, src=filename)
            photo_patient.save()

            # Enregistrez l'image dans un dossier approprié avec le nouveau nom de fichier
            with open('static/images/patient/' + filename, 'wb+') as destination:
                for chunk in profile_picture.chunks():
                    destination.write(chunk)

        return render(request, 'login.html')

    return render(request, 'inscription.html')


def checkLogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if Patient.checkLogin(email, password):
        p = Patient.getPatient(email, password)
        if p.is_actif==1:
            request.session['idSession'] = p.id
            return home(request)
        else:
            request.session['idSession'] = p.id
            return abonnement(request)
    elif Famille.checkLogin(email,password):
        f = Famille.getFamille(email,password)
        request.session['idFamille'] = f.id
        return familleV(request)
    else:
        return render(request, 'login.html')


def familleV(request):
    if 'idFamille' in request.session:
        famille_id = request.session['idFamille']
        famille = Famille.objects.get(id=famille_id)
        membres = famille.patient_set.all()

        context = {
            'famille': famille,
            'membres': membres,
        }
        return render(request, 'descFamille.html', context)
    else:
        return login(request)


def livraison(request):
    return render(request,'livraison.html')


def ajouter_livraison(request):
    if request.method == 'POST':
        datetime_livraison = request.POST['datetime_livraison']
        adresse = request.POST['adresse']
        description = request.POST['description']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']


        livraison = Livraison.objects.create(
            datetime_livraison=datetime_livraison,
            adresse=adresse,
            description=description,
            latitude=latitude,
            longitude=longitude,
            patient_id=request.session['idSession'],
            etat=0
        )


        for key, value in request.session['panier'].items():
            objet_id = key
            quantite = value['quantite']
            obj = Objet.objects.get(id=key)
            prix = obj.prix
            ObjetALivrer.objects.create(
                livraison=livraison,
                objet_id=objet_id,
                quantite=quantite,
                prix=prix
            )

        # Supprimer les objets à livrer de la session
        del request.session['panier']

        return home(request)
    return home(request)
def ajouter_membre(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenoms = request.POST.get('prenoms')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')
        sexe = request.POST.get('sexe')
        date_de_naissance = request.POST.get('date_de_naissance')
        email = request.POST.get('email')
        password = request.POST.get('password')

        famille_id = request.session['idFamille']
        famille = Famille.objects.get(id=famille_id)

        membres = famille.patient_set.all()
        if membres.count() > 3:
            return familleV(request)
        else:
            patient = Patient(
                nom=nom,
                prenoms=prenoms,
                adresse=adresse,
                telephone=telephone,
                sexe=sexe,
                date_de_naissance=date_de_naissance,
                email=email,
                password=password,
                famille=famille,
                is_actif=1
            )

            patient.save()

            if 'profile_picture' in request.FILES:
                profile_picture = request.FILES['profile_picture']
                filename = str(patient.id) + '.' + profile_picture.name.split('.')[-1]  # Nouveau nom de fichier
                photo_patient = PhotoPatient(patient=patient, src=filename)
                photo_patient.save()
                with open('static/images/patient/' + filename, 'wb+') as destination:
                    for chunk in profile_picture.chunks():
                        destination.write(chunk)

    return familleV(request)



def boutique(request):

    objets = Objet.getAllObjet()

    context = {
        'objets':objets
    }

    return render(request, 'boutique.html',context)

def abonnement(request):

    typeAbonnement = TypeAbonnement.objects.all()

    context = {
        'type':typeAbonnement
    }

    return render(request, 'abonnement.html',context)


def listeDiscu(request):
    return render(request, 'Listediscussion.html')

def profilMedecin(request):
    id_medecin = request.GET.get('idMedecin')
    medecin = Medecin.objects.get(id=id_medecin)
    context = {'medecin': medecin}
    return render(request, 'profil.html', context)

from django.http import HttpResponse, JsonResponse


def ajouter_au_panier(request, objet_id):
    # Vérifier si l'objet existe
    try:
        objet = Objet.objects.get(id=objet_id)
    except Objet.DoesNotExist:
        # Gérer le cas où l'objet n'existe pas
        objet = None

    # Vérifier si la session du panier existe déjà
    if 'panier' not in request.session:
        request.session['panier'] = {}  # Créer un dictionnaire vide pour le panier

    panier = request.session['panier']

    # Vérifier si l'objet est déjà dans le panier
    if str(objet_id) in panier:
        # Si l'objet est déjà dans le panier, augmenter la quantité
        panier[str(objet_id)]['quantite'] += 1
    else:
        # Si l'objet n'est pas encore dans le panier, l'ajouter avec une quantité de 1
        panier[str(objet_id)] = {
            'quantite': 1
        }

    # Mettre à jour la session du panier
    request.session['panier'] = panier

    objets = Objet.getAllObjet()

    context = {
        'objets': objets,
        'objet': objet
    }

    return render(request, 'boutique.html', context)



    # Rediriger ou renvoyer une réponse appropriée

from django.shortcuts import redirect

def supprimer(request, objet_id):
    objets = Objet.getAllObjet()
    context = {
        'objets': objets
    }
    
    if 'panier' in request.session:
        panier = request.session['panier']
        if(  panier[str(objet_id)]['quantite'])>1:
          if str(objet_id) in panier:
            panier[str(objet_id)]['quantite'] -= 1
        else:
            del panier[str(objet_id)]

    request.session['panier'] = panier  # Mettre à jour la session du panier

    # Rediriger vers la vue panier.html avec le contexte mis à jour
    return redirect('../../panier', context=context)



def panier(request):
    objets = Objet.getAllObjet()

    tot = Objet.getTotalPanier(request)

    context = {
        'objets':objets,
        'tot':tot
    }
    return render(request, 'panier.html',context)

def viderPanier(request):
    if 'panier' in request.session:
        del request.session['panier']
    
    return render(request,'panier.html')

# def profilMedecin(request):
#     id_medecin = request.GET.get('idMedecin')
#     medecin = Medecin.objects.select_related('specialite').get(id=id_medecin)
#     context = {'medecin': medecin}
#     return render(request, 'ProfilDocteur.html', context)

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


def ajouter_abonnement(request):
    types_abonnement = TypeAbonnement.objects.all()

    context = {
        'type': types_abonnement
    }
    if request.method == 'POST':
        type_abonnement_id = request.POST.get('type_abonnement')
        ref = request.POST.get('ref')
        patient_id = request.session['idSession']  # L'ID du patient associé à l'abonnement

        try:
            type_abonnement = TypeAbonnement.objects.get(id=type_abonnement_id)
            patient = Patient.objects.get(id=patient_id)
            current_datetime = datetime.now()
            date_fin = current_datetime + timedelta(days=31)

            abonnement = Abonnement.objects.create(
                patient=patient,
                type=type_abonnement,
                date_fin=date_fin,
                reference=ref
            )
            return login(request)

        except (TypeAbonnement.DoesNotExist, Patient.DoesNotExist):
            return render(request, 'abonnement.html')
    return render(request, 'abonnement.html', context)


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
    patient = Patient.objects.get(id=idPatient)
    patient.modifierPatient(adresse,tel,ddn)
    return redirect('profil')

def collaboration(request):
    fonctions= FonctionCollab.objects.all()
    context = {'fonctions': fonctions}
    return render(request, 'collaboration.html', context)

def inserer_collab(request):
    nom = request.POST.get('nom')
    prenoms = request.POST.get('prenoms')
    fonc = request.POST.get('fonction')
    bio = request.POST.get('bio')
    fichier = request.FILES.get('fichier')
    fonction = FonctionCollab.objects.get(id=fonc)
    if fichier:
        # Générer un chemin d'enregistrement pour le fichier
        chemin = 'static/upload/' + fichier.name

        # Écrire le fichier sur le serveur
        with open(chemin, 'wb') as f:
            for morceau in fichier.chunks():
                f.write(morceau)
        Collaboration.inserer_collaborateur(nom,prenoms,fonction,bio,fichier)
    collab= Collaboration.objects.latest('id')
    if fonc=='1':
        specialite = Specialite.objects.all()
        context = {
                    'specialites' : specialite,
                    'collab' : collab
                  }
        return render(request, 'formDocteur.html',context)
    else:
        return redirect('collaboration')
    return HttpResponse(fonc)
def inserer_docteur(request):
    idCollab = request.POST.get('collab')
    collab = Collaboration.objects.get(id=idCollab)
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    idSpe = request.POST.get('specialite')
    specialite = Specialite.objects.get(id=idSpe)
    DemandeDocteur.inserer_demande(collab,email,pwd,specialite)
    return redirect('collaboration')
def collabBack(request):
    fonctions = FonctionCollab.objects.all()
    context = {'fonctions': fonctions}
    return render(request, 'collabBack.html', context)

def demande_collab(request):
    idFonction = request.GET.get('idFonction')
    collab = Collaboration.objects.filter(etat=0,fonction=idFonction)
    context = {
        'collabs': collab
    }
    return render(request, 'demandeCollab.html', context)

def collab_EnCours(request):
    idFonction = request.GET.get('idFonction')
    collab = Collaboration.objects.filter(etat=1, fonction=idFonction,date_fin__gte=timezone.now() )
    context = {
        'collabs': collab
    }
    return render(request, 'collabEnCours.html', context)

def accepter_collab(request):
    idCollab = request.GET.get('idCollab')
    collab = Collaboration.objects.select_related('fonction').get(id=idCollab)
    idFonction = collab.fonction.id
    fonction = FonctionCollab.objects.get(id=idFonction)
    collab.accepter_collaboration(fonction)
    demande = DemandeDocteur.objects.get(collaboration_id=idCollab)
    Medecin.create(collab.nom,collab.prenoms,demande.email,demande.password,demande.specialite)
    demande.update()
    return redirect('demande_collab')

def refuser_collab(request):
    idCollab = request.GET.get('idCollab')
    collab = Collaboration.objects.get(id=idCollab)
    collab.refuser_collaboration()
    return redirect('demande_collab')

#--------------------------------------------------DOCTEUR BACK OFFICE--------------------------------------------


def loginDocteur(request):
    return render(request,'loginDocteur.html')
def homeDocteur(request):
    return render(request,'baseDocteur.html')

def ordonnance(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request,'addOrdonnance.html')

def get_patient_suggestions(request):
    search_query = request.GET.get('search', '')
    patients = Patient.objects.filter(nom__icontains=search_query).values('id','nom', 'prenoms')
    suggestions = list(patients)
    return JsonResponse(suggestions, safe=False)

def checkLoginDoc(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if Medecin.checkLogin(email, password):
        d = Medecin.getMedecin(email,password)
        request.session['idSessionDoc'] = d.id
        return homeDocteur(request)

    return loginDocteur(request)

from django.shortcuts import render, redirect


def create_consultation(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        date_consultation = request.POST.get('date_consultation')
        symptomes = request.POST.get('symptomes')
        diagnostic = request.POST.get('diagnostic')
        idP = request.POST.get('idPatient')
        medocs = request.POST.getlist('medocs[]')
        prises = request.POST.getlist('prise[]')
        remarques = request.POST.getlist('remarque[]')


        patient = Patient.objects.get(id=idP)
        idDoc = request.session['idSessionDoc']
        docteur = Medecin.objects.get(id=idDoc)
        # Créer une instance de Consultation et l'enregistrer dans la base de données
        consultation = Consultation.objects.create(medecin=docteur,date_consultation=date_consultation, symptomes=symptomes, diagnostic=diagnostic, patient=patient)

        # Créer des instances d'Ordonnance et les lier à la consultation
        for i in range(len(medocs)):
            ordonnance = Ordonnance.objects.create(consultation=consultation, medocs=medocs[i], prise=prises[i], remarque=remarques[i])

        # Rediriger vers une page de succès ou faire autre chose

    return homeDocteur(request)


