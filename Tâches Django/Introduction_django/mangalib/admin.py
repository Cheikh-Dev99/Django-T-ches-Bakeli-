from django.contrib import admin
from .models import Auteur, Livre

@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
  list_display = ('prenom', 'nom', 'date_de_naissance')

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
  fieldsets = [
    ('information manga', {'fields': ['titre', 'auteur', 'genre', 'annee_edition']}),
    ('information magasin', {'fields': ['quantite', 'prix']})
  ]
  list_display = (
    'titre',
    'auteur',
    'genre',
    'annee_edition',
    'prix',
    'quantite'
  )
  list_filter = ['auteur']
  search_fields = ['titre']
  list_per_page = 5
