from django.urls import path
from . import views

app_name = "mangalib"

urlpatterns = [
    path('', views.index, name='formulaire')
]
