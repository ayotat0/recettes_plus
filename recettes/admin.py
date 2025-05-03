from django.contrib import admin
from .models import Recette, Categorie

admin.site.site_header = "Administration Recettes+"
admin.site.site_title = "Recettes+ Admin"
admin.site.index_title = "Bienvenue dans l’admin de Recettes+"

class RecetteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'temps_preparation', 'difficulte', 'date_creation')
    list_filter = ('categorie', 'difficulte', 'date_creation')
    search_fields = ('titre', 'description', 'ingredients')
    ordering = ('-date_creation',)

admin.site.register(Recette, RecetteAdmin)
admin.site.register(Categorie)