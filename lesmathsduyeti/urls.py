"""lesmathsduyeti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from trombinoscoop.views import welcome,login,register,index
from interrogateur.views import interrogateur, bilan, interrogateur_accueil, nouvelle_note, deconnexion
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/', welcome),
    url(r'^register/', register),
    # url(r'^', index), # Pour tester Bootstrap
    url(r'^interrogateur/$', interrogateur_accueil, name='Interrogateur_accueil'),
    url(r'^interrogateur/(?P<classe>[0-9])/$', interrogateur, name='interrogateur'),
    url(r'^interrogateur/bilan/$', bilan, name='Interrogateur_bilan'),
    url(r'^interrogateur/nouvelle_note/(?P<classe>[0-9])/(?P<id_eleve>[0-9])$', nouvelle_note,
        name='Interrogateur_nouvelle_note'),
    # url(r'^interrogateur/login/$', connexion, name='connexion'),
    url(r'^connexion/$', auth_views.login, {'template_name': 'interrogateur_login.html'}, name='connexion'),
    url(r'^deconnexion$', deconnexion, name='deconnexion'),
]
