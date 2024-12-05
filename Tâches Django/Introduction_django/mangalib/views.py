from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Auteur, Livre
from .forms import LivreForm

def index(request):
    contexte = {
        "Livres": Livre.objects.all()
    }
    return render(request, 'mangalib/index.html', contexte)

def show(request, Livre_id):
        context = {
            "Livre": get_object_or_404(Livre, pk = Livre_id)
        }
        return render(request, "mangalib/show.html", context)

def add(request):
    if request.method == "POST":
        form = LivreForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("mangalib:index3")
    else:
        form = LivreForm()
        
    return render(request, "mangalib/Livre-form.html", {"form": form})

def edit(request, Livre_id):
    livre_instance = Livre.objects.get(pk = Livre_id)

    if request.method == "POST":
        form = LivreForm(request.POST, instance = livre_instance)

        if form.is_valid():
            form.save()
            return redirect("mangalib:index3")
    else:
        form = LivreForm(instance = livre_instance)
        
    return render(request, "mangalib/Livre-form.html", {"form": form})

def supp(request, Livre_id ):
    livre_instance = Livre.objects.get(pk = Livre_id)
    livre_instance.delete()
    return redirect("mangalib:index3")
