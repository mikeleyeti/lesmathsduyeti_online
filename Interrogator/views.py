from django.shortcuts import render_to_response
from Interrogator.models import Classe, Eleve
from random import randint
from django.shortcuts import render

# Create your views here.
def interrogator(request, classe):
    id_de_la_classe = classe
    nom_de_la_classe = Classe.objects.filter(id=id_de_la_classe)[0]
    nombre_d_eleves = Eleve.objects.filter(classe_id=id_de_la_classe).count()
    nombre_aleatoire = randint(0, nombre_d_eleves - 1)
    eleve_designe = Eleve.objects.filter(classe_id=id_de_la_classe)[nombre_aleatoire].affichage()
    return render_to_response('interrogator.html',
                              {'id': id_de_la_classe, 'nom': nom_de_la_classe, 'nombre_eleves': nombre_d_eleves,
                               'nombre_alea': nombre_aleatoire, 'eleve_designe': eleve_designe})
