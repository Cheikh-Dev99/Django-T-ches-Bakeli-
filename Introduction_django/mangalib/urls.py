from django.urls import path
from . import views

app_name = "mangalib"

urlpatterns = [
    path('', views.index, name='index3'),
    path('<int:Livre_id>/', views.show, name='show'),
    path('aouter-livre/', views.add, name='add'),
    path('modifier-livre/', views.edit, name='edit'),
    path('supprimer-livre/', views.supp, name='supp'),
]
