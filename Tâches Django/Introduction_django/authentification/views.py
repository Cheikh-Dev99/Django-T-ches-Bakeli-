from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# -------------------------
def register_user(request):
  pass

# ----------------------
def login_user(request):
  if request.method == 'POST':
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username = username, password = password)

    if user is not None:
      login(request, user)
      return redirect("mangalib:index3")
    else:
      messages.info(request, "Informations d'identifications incorrecte")

  form = AuthenticationForm()
  return render(request, "authentification/login.html", {"form": form})

# -----------------------
def logout_user(request):
  logout(request)
  return redirect("mangalib:index3")


