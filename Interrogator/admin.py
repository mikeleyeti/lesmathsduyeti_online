from django.contrib import admin

# Register your models here.
from Interrogator.models import Classe, Eleve


class EleveAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'classe', 'note')
    list_filter = ('classe',)
    ordering = ('nom',)
    search_fields = ('nom', 'prenom')


admin.site.register(Eleve, EleveAdmin)
admin.site.register(Classe)
