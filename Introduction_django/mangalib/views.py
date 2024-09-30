from django.shortcuts import render

def index(request):
  contexte = {'titre': 'Bienvenue sur Mangalib',
              'message': 'MangaLib est un site web destiner aux amoureux du Mangas'
  }
  return render(request, 'mangalib/index.html', contexte)
