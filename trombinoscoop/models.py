from django.db import models


# Personne simplifiée
class Personne(models.Model):
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_de_naissance = models.DateField()
    couriel = models.EmailField()
    tel_fixe = models.CharField(max_length=20)
    tel_mobile = models.CharField(max_length=20)
    mot_de_passe = models.CharField(max_length=32)


