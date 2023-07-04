from django.db import models, IntegrityError

from django.db.models import Sum, F, ExpressionWrapper, FloatField
from django.core.exceptions import ValidationError

from .TypeStatistique import TypeStatistique
from .Caisse import Caisse

class Statistique(models.Model):
    type = models.ForeignKey("TypeStatistique", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False) 
    designation = models.CharField(max_length=255)
    prix_unitaire = models.FloatField()
    quantite = models.IntegerField()
    montant = models.FloatField()
    
    class Meta:
        db_table = 'statistique'

    def set_type(self,type_statistique):
        self.type=type_statistique

    def set_date(self, date):
        self.date=date

    def set_designation(self, designation):
        self.designation=designation
    
    def set_prix(self, prix):
        self.prix_unitaire=prix
    
    def set_quantite(self, quantite):
        self.quantite=quantite
    
    def set_montant(self, montant):
        self.montant=montant
    
    @staticmethod
    def get_statistiques_par_type(id_type):
        type_statistique = TypeStatistique.objects.get(id=id_type)
        statistiques = Statistique.objects.filter(type=type_statistique)
        statistiques = statistiques.annotate(montant_total=ExpressionWrapper(F('quantite') * F('prix_unitaire'), output_field=FloatField()))
        total_depenses = statistiques.aggregate(total_montant=Sum('montant_total')).get('total_montant')
        return statistiques , total_depenses

    @staticmethod
    def getStatDepense():
        return Statistique.get_statistiques_par_type(id_type=1)

    @staticmethod
    def getStatRecette():
        return Statistique.get_statistiques_par_type(id_type=2)

    @staticmethod
    def create(id_type, date, designation, prix_unitaire, quantite):
        statistique = Statistique()
        montant = prix_unitaire * quantite
        type_statistique = TypeStatistique.objects.get(id=id_type)

        nouveau_caisse = Caisse()
        caisse = Caisse.get_last()

        if id_type == 1:
            nouveau_caisse.set_date(date)
            nouveau_caisse.set_montant(caisse.montant - montant)
            nouveau_caisse.save()
        else:
            caisse.set_date(date)
            caisse.set_montant(caisse.montant + montant)
            caisse.save()

        statistique.set_type(type_statistique)
        statistique.set_date(date)
        statistique.set_designation(designation)
        statistique.set_prix(prix_unitaire)
        statistique.set_quantite(quantite)
        statistique.set_montant(montant)
        statistique.clean_fields()
        try:
            statistique.save()
        except IntegrityError:
            raise ValidationError("Cette statistique existe déjà")
        return statistique, caisse


    def update(self, date, designation, prix_unitaire, quantite, montant):
        self.set_date(date)
        self.set_designation(designation)
        self.set_prix(prix_unitaire)
        self.set_quantite(quantite)
        self.set_montant(montant)
        self.clean_fields()
        try:
            self.save()
        except IntegrityError:
            raise ValidationError("Le medecin " + str(nom) + " " + str(prenoms) + " existe déjà")
        return self

    def remove(self):
        self.delete()
        return 0

    @staticmethod
    def get_depense_par_date(mois, annee):
        statistiques = Statistique.objects.filter(type_id=1, date__month=mois, date__year=annee)
        statistiques = statistiques.annotate(montant_total=ExpressionWrapper(F('quantite') * F('prix_unitaire'), output_field=FloatField()))
        total_depenses = statistiques.aggregate(total_montant=Sum('montant_total')).get('total_montant')
        return statistiques, total_depenses

    @staticmethod
    def get_recette_par_date(mois, annee):
        statistiques = Statistique.objects.filter(type_id=2, date__month=mois, date__year=annee)
        statistiques = statistiques.annotate(montant_total=ExpressionWrapper(F('quantite') * F('prix_unitaire'), output_field=FloatField()))
        total_recettes = statistiques.aggregate(total_montant=Sum('montant_total')).get('total_montant')
        return statistiques, total_recettes


    