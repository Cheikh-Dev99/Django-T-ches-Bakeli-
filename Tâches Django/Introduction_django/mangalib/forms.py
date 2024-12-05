from django import forms
from .models import Auteur, Livre

class LivreForm(forms.ModelForm):
    auteur = forms.ModelChoiceField(queryset= Auteur.objects.all(), label= "Auteur")

    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'genre', 'annee_edition', 'prix', 'quantite']
        labels = {
            'titre': 'Titre',
            'genre': 'Genre',
            'annee_edition': "Annee d'edition",
            'prix': 'Prix',
            'quantite': 'Quantité' 
        }
