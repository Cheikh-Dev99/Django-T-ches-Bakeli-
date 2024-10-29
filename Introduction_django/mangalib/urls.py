from django.urls import path
from . import views

app_name = "mangalib"

urlpatterns = [
    path('', views.index, name='index3'),
    path('<int:Livre_id>/', views.show, name='show')
]
