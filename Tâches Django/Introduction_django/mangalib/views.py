from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import datetime
import random
from utils.citations import citations
from .models import Auteur, Livre

# def index(request):
#     D1 = datetime.datetime.now()
#     D2 = D1 - datetime.timedelta(minutes=random.randint(1, 60))  # D2 est 30 minutes avant D1
#     mesCitations = citations
#     contexte = {
#         'titre': 'Bienvenue sur Mangalib',
#         'titre2': 'Django : Balises & Filtres',
#         'titre3': 'Django : Balises & Filtres : personalisation',
#         'message': "Django est un framework de développement web qui facilite la  création d'applications web en Python.",
#         'message1': 'Hello World !',
#         "D1": D1,
#         "D2": D2,
#         'citations': mesCitations,
#         'username': "Cheikh",
#         'numberOfNews': random.randint(0, 100),
#         'link': "http://mesfilmsetseries.sn/index.html?categorie=action&p=2",
#         'text': "Vous pouvez retrouver plus de films et de series sur http://Film&Serie.sn"
#     }
#     return render(request, 'mangalib/index.html', contexte)
def index(request):
    context = {
        "titre": "Bienvenue sur Mangalib",
        "Livres": Livre.objects.all().order_by("titre"),
    }
    return render(request, "mangalib/index3.html", context)

def show(request, Livre_id):
        context = {
            "Livre": get_object_or_404(Livre, pk = Livre_id)
        }
        return render(request, "mangalib/show.html", context)
    
def add(request):
    auteur_instance = Auteur.objects.get(prenom = "Akira", nom = "Toriyama")
    livre_instance = Livre.objects.create(
        titre = "Dragon Ball Z", 
        auteur = auteur_instance, 
        genre = "shōnen", 
        annee_edition = 1989,
        prix = 12.36,
        quantite = 15,
    )
    return redirect("mangalib:index3")

def edit(request):
    livre_instance = Livre.objects.get(titre = "Dragon Ball")
    livre_instance.titre = "Dragon Ball Super"
    livre_instance.annee_edition = 2015
    livre_instance.save()
    return redirect("mangalib:index3")

def supp(request):
    livre_instance = Livre.objects.filter(titre = "titre_test")
    livre_instance.delete()
    return redirect("mangalib:index3")
