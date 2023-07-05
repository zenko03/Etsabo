from django.db import models

class Caisse(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    montant = models.FloatField()

    class Meta:
        db_table = 'caisse'

    def set_date(self, date):
        self.date=date

    def set_montant(self, montant):
        self.montant=montant

    @staticmethod
    def get_by_date(date):
        caisse = Caisse.objects.get(date=date)
    
    @staticmethod
    def get_last():
        caisses = Caisse.objects.all()
        return caisses[len(caisses)-1]


