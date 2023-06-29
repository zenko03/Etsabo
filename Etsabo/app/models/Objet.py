from django.core.exceptions import ValidationError
from django.db import models, IntegrityError

class Objet(models.Model):
    nom_objet = models.CharField(max_length=70)
    prix = models.FloatField()
    
    class Meta:
        db_table = 'objet'

    def set_nom(self,nom):
        self.nom_objet= nom

    def set_prix(self,prix):
        self.prix = prix

    @staticmethod
    def getAllObjet():
        return Objet.objects.all().prefetch_related('photoobjet_set')

    @staticmethod
    def getAll():
        return Objet.objects.all()

    @staticmethod
    def create(nom, prix):
        objet = Objet()
        objet.set_nom(nom)
        objet.set_prix(prix)
        try:
            objet.save()
        except IntegrityError:
            raise ValidationError("L'objet " + str(nom) + " existe déjà")
        return objet

    def update(self, nom, prix):
        self.set_nom(nom)
        self.set_prix(prix)
        self.clean_fields()
        try:
            self.save()
        except IntegrityError:
            raise ValidationError("L'objet " + str(nom) + " existe déjà")
        return self

    def remove(self):
        self.delete()
        return 0

    @staticmethod
    def getTotalPanier(request):
        total = 0
        if 'panier' in request.session:
            panier = request.session['panier']
        
        for key, value in panier.items():
            objet = Objet.objects.get(id=int(key))
            prix_unitaire = objet.prix
            quantite = value['quantite']
            total += prix_unitaire * quantite

        return total


