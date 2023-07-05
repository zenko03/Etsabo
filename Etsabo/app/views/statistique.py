from django.shortcuts import render, redirect, HttpResponse
from app.models import Statistique
from app.models import Caisse
from app.models import Abonnement
from app.models import Patient
from app.models import Objet
from app.models import PhotoObjet
from django.db.models import Sum
from json import dump

def statistiques_depenses(request):
    caisse= Caisse.get_last()     

    if request.method == 'POST':
        month_mapping = {
        'Janvier': 1,
        'Février': 2,
        'Mars': 3,
        'Avril': 4,
        'Mai': 5,
        'Juin': 6,
        'Juillet': 7,
        'Aout': 8,
        'Septembre': 9,
        'Octobre': 10,
        'Novembre': 11,
        'Decembre': 12}

        mois =request.POST.get('mois')
        mois_int = month_mapping.get(mois)

        annee =request.POST.get('annee')

        statistiques_depenses , total_depenses= Statistique.get_depense_par_date( mois_int, annee)

        context = {
            'statistiques': statistiques_depenses,
            'total_depenses': total_depenses,
            'mois': mois,
            'annee': annee,
            'caisse':caisse
        }
    else :         
        statistiques_depenses, total_depenses = Statistique.getStatDepense()

        context = {
            'statistiques': statistiques_depenses,
            'total_depenses': total_depenses,
            'caisse':caisse

        }
    return render(request, 'statistique.html', context)

def ajout_depense(request):
    print(request.POST)
    if request.method == 'POST':
        date = request.POST.get('date')
        designation = request.POST.get('designation')
        prix_unitaire = float(request.POST.get('prix_unitaire'))
        quantite = int(request.POST.get('quantite'))
        
        print(prix_unitaire)
        # Appeler la fonction create pour créer la statistique
        Statistique.create(id_type=1, date=date, designation=designation,prix_unitaire=prix_unitaire, quantite=quantite)
        
        return redirect('ajout_depense')  # Rediriger vers la page des statistiques après l'ajout
    
    return render(request, 'ajout_depense.html')

def statistiques_recettes(request):
    caisse= Caisse.get_last()   
    # Appel de la méthode getStatRecette()
    if request.method == 'POST':
        month_mapping = {
        'Janvier': 1,
        'Février': 2,
        'Mars': 3,
        'Avril': 4,
        'Mai': 5,
        'Juin': 6,
        'Juillet': 7,
        'Aout': 8,
        'Septembre': 9,
        'Octobre': 10,
        'Novembre': 11,
        'Decembre': 12}

        mois =request.POST.get('mois')
        mois_int = month_mapping.get(mois)

        annee =request.POST.get('annee')

        statistiques_recettes , total_recettes= Statistique.get_recette_par_date( mois_int, annee)

        context = {
            'recettes': statistiques_recettes,
            'total_recettes': total_recettes,
            'mois': mois,
            'annee': annee,
            'caisse':caisse
        }
    else :
        statistiques_recettes, total_recettes = Statistique.getStatRecette()
        context = {
            'recettes': statistiques_recettes,
            'total_recettes': total_recettes,
            'caisse':caisse 
        }
    return render(request, 'recettes.html', context)

def remove_statistique(request, statistique_id):
    statistique = Statistique.objects.get(id=statistique_id)
    statistique.delete()

    return redirect('../../../depenses')

def remove_recette(request, recette_id):
    statistique = Statistique.objects.get(id=recette_id)
    statistique.delete()
    return redirect('../../../depenses')




def activerCompte(request, patientId):
    patient = Patient.objects.get(id=patientId)
    patient.is_actif=1;
    patient.save()
    return demandeAb(request)


def demandeAb(request):

    allAb = Abonnement.getAbonnementEncours()

    context = {
        'all':allAb
    }

    return render(request,'demandeAbonnement.html',context)

def addObjet(request):
    return render(request,'ajouterObjet.html')

def creerObjet(request):
    if request.method == 'POST':
        nom = request.POST.get('nomObjet')
        prix = request.POST.get('prix')

        obj = Objet(nom_objet=nom,prix=prix)

        obj.save()

        print("pppppppppp")
        if 'objetSary' in request.FILES:
            profile_picture = request.FILES['objetSary']
            filename = str(obj.id) + '.' + profile_picture.name.split('.')[-1]  # Nouveau nom de fichier
            photo_obj = PhotoObjet(objet=obj, src=filename)
            photo_obj.save()

            # Enregistrez l'image dans un dossier approprié avec le nouveau nom de fichier
            with open('static/images/objets/' + filename, 'wb+') as destination:
                for chunk in profile_picture.chunks():
                    destination.write(chunk)

    print("ppppppppppNo")
    return addObjet(request)