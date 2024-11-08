from django.db import models

class Auteur(models.Model):
  prenom = models.CharField(max_length=100)
  nom = models.CharField(max_length=100)
  date_de_naissance = models.DateField(null=True, blank=True)
  
  def __str__(self):
    return f"{self.prenom} {self.nom}"
  
  class Meta:
    verbose_name = "Auteur"
    verbose_name_plural = "Auteurs"
  
class Livre(models.Model):
  titre = models.CharField(max_length=200, unique=True)
  auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
  genre = models.CharField(max_length=50)
  annee_edition = models.PositiveIntegerField()
  prix = models.DecimalField(max_digits=10, decimal_places=2)
  quantite = models.IntegerField(default=1)
  
  def __str__(self):
    return self.titre
  
  class Meta:
    verbose_name = "Livre"
    verbose_name_plural = "Livres"
