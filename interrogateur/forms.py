from django import forms
from interrogateur.models import Classe


# Données de test pour afficher un formulaire CHOICES
# MY_CHOICES = (
#     ('1', 'Option 1'),
#     ('2', 'Option 2'),
#     ('3', 'Option 3'),
# )

def obtenir_liste_des_classes():
    choices_list = []
    for i in Classe.objects.all():
        choices_list.append((i.id, i.affichage()))
    return choices_list


class Choix_de_la_classe(forms.Form):
    classe_field = forms.ChoiceField(choices=obtenir_liste_des_classes())
    # classe_field = forms.ChoiceField(choices=MY_CHOICES)


changements_note = (
    ('-1', '-1'),
    ('0', '0'),
    ('+1', '+1'),
)


class Changement_de_note(forms.Form):
    changements_note_field = forms.ChoiceField(widget=forms.RadioSelect, choices=changements_note)
    eleve = 'nelly'

    # classe_field = forms.ChoiceField(choices=MY_CHOICES)


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
