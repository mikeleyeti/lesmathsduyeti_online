from django.db import models

# Create your models here.
class Classe(models.Model):
    # Définiton des champs
    def __str__(self):
        return "Classe de " + self.niveau + " " + self.nom

    def affichage(self):
        return "Classe de " + self.niveau + " " + self.nom
    niveaux = (
        ('6', 'Sixième'),
        ('5', 'Cinquième'),
        ('4', 'Quatrième'),
        ('3', 'Troisième'),
    )
    niveau = models.CharField(max_length=1, choices=niveaux)
    nom = models.CharField(max_length=30)



class Eleve(models.Model):
    def __str__(self):
        return self.nom.upper() + " " + self.prenom.capitalize()

    def affichage(self):
        return self.nom.upper() + " " + self.prenom.capitalize()

    def ajouter_un_point(self):
        self.note -= 1
        self.save()

    def enlever_un_point(self):
        self.note -= 1
        self.save()

    classe = models.ForeignKey(Classe)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_de_naissance = models.DateField()
    note = models.IntegerField(default=10)
    nombre_d_interrogation_orale = models.IntegerField(default=0)
