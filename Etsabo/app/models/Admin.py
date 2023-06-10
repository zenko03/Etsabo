from django.db import models

class Admin(models.Model):
    nom = models.CharField(max_length=30)
    email = models.EmailField(default="")
    password = models.CharField(max_length=30,default="")

    class Meta:
        db_table = "Admin"

    def __init__(self, nom, email, password, *args, **kwargs):
        super(Admin, self).__init__(*args, **kwargs)
        self.nom = nom
        self.email = email
        self.password = password

    @classmethod
    def inscription(cls, nom, email, password):
        admin = cls(nom=nom, email=email, password=password)
        admin.save()
        return admin

    @classmethod
    def login(cls, email, password):
        try:
            admin = cls.objects.get(email=email, password=password)
            return admin
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_admin_by_id(cls, admin_id):
        try:
            admin = cls.objects.get(id=admin_id)
            return admin
        except cls.DoesNotExist:
            return None


    