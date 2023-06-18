from django.shortcuts import render
from app.models import Medecin
from app.models import Publicite


def home(request):
    medecins = Medecin.objects.all()
    pubs = Publicite.objects.all()
    random_pubs = Publicite.get_random_Pub(pubs, 3)
    context = {
        'medecins': medecins,
        'pubs': random_pubs,
    }
    return render(request, 'accueil.html',context)

def boutique(request):
    return render(request, 'boutique.html')

def listeDiscu(request):
    return render(request, 'Listediscussion.html')

def profilMedecin(request):
    id_medecin = request.GET.get('idMedecin')
    medecin = Medecin.objects.get(id=id_medecin)
    context = {'medecin': medecin}
    return render(request, 'profil.html', context)

