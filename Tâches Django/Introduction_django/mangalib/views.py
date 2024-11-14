from django.shortcuts import render


def index(request):
    context = {
        "titre": "Bienvenue sur Mangalib",
    }
    
    return render(request, "mangalib/formulaire.html", context)

