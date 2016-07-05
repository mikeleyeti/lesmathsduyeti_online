from django.shortcuts import render_to_response
from datetime import datetime
from django.http import HttpResponseRedirect
from trombinoscoop.forms import LoginForm

# Create your views here.
def welcome(request):
    return render_to_response('welcome.html', {'date_actuelle': datetime.now()})

# def login(request):
#     # Test si formulaire a été envoyé
#     if len(request.GET) > 0:
#         # Test si les paramètres attendus ont été transmis
#         if 'email' not in request.GET or 'password' not in request.GET:
#             error = "Veuillez entrer une adresse de courriel et un mot de passe."
#             return render_to_response('login.html', {'error': error})
#         else:
#             email = request.GET['email']
#             password = request.GET['password']
#             # Test si le mot de passe est le bon
#             if password != 'sesame' or email != 'pierre@lxs.be':
#                 error = "Adresse de courriel ou mot de passe erroné."
#                 return render_to_response('login.html', {'error': error})
#             # Tout est bon, on va à la page d'accueil
#             else:
#                 return HttpResponseRedirect('/welcome')
#     # Le formulaire n'a pas été envoyé
#     else:
#         return render_to_response('login.html')

def login(request):
    # Test si formulaire a été envoyé
    if len(request.GET) > 0:
        form = LoginForm(request.GET)
        if form.is_valid():
            return HttpResponseRedirect('/welcome')
        else:
            return render_to_response('login.html', {'form': form})
    # Le formulaire n'a pas été envoyé
    else:
        form = LoginForm()
        return render_to_response('login.html', {'form': form})
