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
from Interrogator.views import interrogator, bilan, interrogator_accueil, nouvelle_note

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/', welcome),
    url(r'^login/', login),
    url(r'^register/', register),
    # url(r'^', index), # Pour tester Bootstrap
    url(r'^Interrogator/$', interrogator_accueil, name='Interrogator_accueil'),
    url(r'^Interrogator/(?P<classe>[0-9])/$', interrogator, name='Interrogator'),
    url(r'^Interrogator/bilan/$', bilan, name='Interrogator_bilan'),
    url(r'^Interrogator/nouvelle_note/(?P<classe>[0-9])/(?P<id_eleve>[0-9])$', nouvelle_note,
        name='Interrogator_nouvelle_note'),
]
