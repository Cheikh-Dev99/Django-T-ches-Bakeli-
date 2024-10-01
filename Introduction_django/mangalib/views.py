from django.shortcuts import render
import datetime
import random
from utils.citations import citations

def index(request):
    D1 = datetime.datetime.now()
    D2 = D1 - datetime.timedelta(minutes=random.randint(1, 60))  # D2 est 30 minutes avant D1
    mesCitations = citations
    contexte = {
        'titre': 'Bienvenue sur Mangalib',
        'titre2': 'Django : Balises & Filtres',
        'message': "Django est un framework de développement web qui facilite la  création d'applications web en Python.",
        'message1': 'Hello World !',
        "D1": D1,
        "D2": D2,
        'citations': mesCitations,
        'username': "Cheikh",
        'numberOfNews': random.randint(0, 100),
        'link': "http://mesfilmsetseries.sn/index.html?categorie=action&p=2",
        'text': "Vous pouvez retrouver plus de films et de series sur http://Film&Serie.sn"
    }
    return render(request, 'mangalib/index.html', contexte)
