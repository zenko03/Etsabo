from django.shortcuts import render
from app.models import Medecin
from app.models import Publicite
from app.models import ConseilsSanitaire
from app.models import Objet
from django.contrib.sessions.models import Session


def home(request):
    medecins = Medecin.objects.all()
    pubs = Publicite.objects.all()
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
    medecin = Medecin.objects.get(id=id_medecin)
    context = {'medecin': medecin}
    return render(request, 'profil.html', context)

from django.http import HttpResponse

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