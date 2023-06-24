
from django.utils import timezone
from django.shortcuts import render
from app.models import Medecin
from app.models import Publicite
from app.models import ConseilsSanitaire
from app.models import Objet


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
    context = {'medecin': medecin}
    return render(request, 'ProfilDocteur.html', context)
