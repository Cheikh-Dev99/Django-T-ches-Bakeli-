from django.contrib import admin
from .models import Auteur, Livre

class LivreAdmin(admin.ModelAdmin):
  list_display = ('titre', 'auteur', 'genre', 'annee_edition' 'prix', 'quantite')

admin.site.register(Auteur)
admin.site.register(Livre, LivreAdmin)
