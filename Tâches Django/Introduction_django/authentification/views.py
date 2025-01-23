from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

# ----------- Inscription --------------
def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Inscription réussie. Vous pouvez maintenant vous connecter.")
            return redirect('authentification:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            messages.error(
                request, "Erreur lors de l'inscription. Veuillez vérifier les informations fournies.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'authentification/register.html', {'form': form})
# ---------- Connexion ------------
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("mangalib:index3")
        else:
            messages.info(
                request, "Informations d'identifications incorrectes")

    form = AuthenticationForm()
    return render(request, "authentification/login.html", {"form": form})
# ---------- Déconnexion -----------
def logout_user(request):
    logout(request)

    return redirect("authentification:login")
