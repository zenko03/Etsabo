from django.shortcuts import render, redirect, HttpResponse
from ..models import Statistique
# from ..models import TypeStatistique
# from ..models import Caisse
from json import dump

def statistiques_depenses(request):
    # Appel de la méthode getStatDepense()
    statistiques_depenses, total_depenses = Statistique.getStatDepense()

    context = {
        'statistiques': statistiques_depenses,
        'total_depenses': total_depenses
    }
    return render(request, 'statistique.html', context)

# def statistiques_recettes(request):
#     # Appel de la méthode getStatRecette()
#     statistiques_recettes, total_recettes = Statistique.getStatRecette()

#     context = {
#         'statistiques': statistiques_recettes,
#         'total_recettes': total_recettes
#     }
#     return render(request, 'statistiques_recettes.html', context)

# def statistiques_depenses_par_date(request, mois, annee):
#     statistiques_depenses = Statistique.get_depense_par_date(1, mois, annee)
#     total_depenses = statistiques_depenses.aggregate(total_montant=Sum('montant_total')).get('total_montant')

#     context = {
#         'statistiques': statistiques_depenses,
#         'total_depenses': total_depenses,
#         'mois': mois,
#         'annee': annee
#     }
#     return render(request, 'statistiques_depenses_par_date.html', context)

# def statistiques_recettes_par_date(request, mois, annee):
#     statistiques_recettes = Statistique.get_recette_par_date(2, mois, annee)
#     total_recettes = statistiques_recettes.aggregate(total_montant=Sum('montant_total')).get('total_montant')

#     context = {
        
#         'statistiques': statistiques_recettes,
#         'total_recettes': total_recettes,
#         'mois': mois,
#         'annee': annee
#     }
#     return render(request, 'statistiques_recettes_par_date.html', context)

