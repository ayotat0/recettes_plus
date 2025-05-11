from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Recette(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    etapes = models.TextField()
    temps_preparation = models.IntegerField(help_text="Temps en minutes")
    difficulte = models.CharField(max_length=50, choices=[('Facile', 'Facile'), ('Moyen', 'Moyen'), ('Difficile', 'Difficile')])
    date_creation = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recettes')
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True, related_name='recettes')
    def __str__(self):
        return self.titre