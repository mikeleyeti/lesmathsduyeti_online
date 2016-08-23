from django.shortcuts import render_to_response, HttpResponseRedirect, render
from Interrogator.models import Classe, Eleve
from Interrogator.forms import Choix_de_la_classe, Changement_de_note
from random import randint

# Create your views here.


def interrogator(request, classe):
    id_de_la_classe = classe
    nom_de_la_classe = Classe.objects.filter(id=id_de_la_classe)[0]
    nombre_d_eleves = Eleve.objects.filter(classe_id=id_de_la_classe).count()
    nombre_aleatoire = randint(0, nombre_d_eleves - 1)
    objet_eleve_designe = Eleve.objects.filter(classe_id=id_de_la_classe)[nombre_aleatoire]
    eleve_designe = Eleve.objects.filter(classe_id=id_de_la_classe)[nombre_aleatoire].affichage()
    note = Eleve.objects.filter(classe_id=id_de_la_classe)[nombre_aleatoire].note
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        # form_note = Changement_de_note(request.POST)  # Nous reprenons les données
        # if form_note.is_valid(): # Nous vérifions que les données envoyées sont valides
        #     # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
        #     evolution_note=form_note.cleaned_data['changements_note_field']
        #     if evolution_note=='-1':
        #         objet_eleve_designe.note-=1
        #         objet_eleve_designe.save()
        #     elif evolution_note=='+1':
        #         objet_eleve_designe.note+=1
        #         objet_eleve_designe.save()
        #     eleves_classe_choisie=Eleve.objects.filter(classe=id_de_la_classe).order_by('nom','prenom')
        #     envoi = True
        return render(request, 'nouvelle_note_interrogator.html', locals())
    else:  # Si ce n'est pas du POST, c'est probablement une requête GET
        form = Changement_de_note()  # Nous créons un formulaire vide
        return render(request, 'interrogator.html', locals())


# def bilan(request):
#     if len(request)>0
#         form = Choix_de_la_classe(request.GET)
#         if form.is_valid():
#
#     return render_to_response('bilan_interrogator.html',locals())

def bilan(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = Choix_de_la_classe(request.POST)  # Nous reprenons les données
        if form.is_valid():  # Nous vérifions que les données envoyées sont valides
            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
            classe_choisie = form.cleaned_data['classe_field']
            eleves_classe_choisie = Eleve.objects.filter(classe=classe_choisie).order_by('nom', 'prenom')
            envoi = True
    else:  # Si ce n'est pas du POST, c'est probablement une requête GET
        form = Choix_de_la_classe()  # Nous créons un formulaire vide
    return render(request, 'bilan_interrogator.html', locals())


def interrogator_accueil(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = Choix_de_la_classe(request.POST)  # Nous reprenons les données
        if form.is_valid():  # Nous vérifions que les données envoyées sont valides
            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
            classe_choisie = form.cleaned_data['classe_field']
            classe = form.cleaned_data['classe_field']
            envoi = True
            return HttpResponseRedirect(classe)
    else:  # Si ce n'est pas du POST, c'est probablement une requête GET
        form = Choix_de_la_classe()  # Nous créons un formulaire vide
    return render(request, 'accueil_interrogator.html', locals())


def nouvelle_note(request, classe, id_eleve):
    objet_eleve_designe = Eleve.objects.filter(classe_id=int(classe))[int(id_eleve)]
    eleve_designe = Eleve.objects.filter(classe_id=int(classe))[int(id_eleve)].affichage()
    nom_de_la_classe = Classe.objects.filter(id=int(classe))[0]
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form_note = Changement_de_note(request.POST)  # Nous reprenons les données
        if form_note.is_valid():  # Nous vérifions que les données envoyées sont valides
            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
            evolution_note = form_note.cleaned_data['changements_note_field']
            if evolution_note == '-1':
                objet_eleve_designe.note -= 1
                objet_eleve_designe.save()
            elif evolution_note == '+1':
                objet_eleve_designe.note += 1
                objet_eleve_designe.save()
            eleves_classe_choisie = Eleve.objects.filter(classe=int(classe)).order_by('nom', 'prenom')
            envoi = True
            nouvelle_note = objet_eleve_designe.note
        return render(request, 'nouvelle_note_interrogator.html', locals())
    return render(request, 'nouvelle_note_interrogator.html', locals())
