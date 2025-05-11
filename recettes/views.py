from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recette
from .forms import RecetteForm

def home(request):
    return render(request, 'recettes/home.html')

@login_required
def liste_recettes(request):
    recettes = Recette.objects.filter(auteur=request.user).order_by('-date_creation')
    return render(request, 'recettes/liste.html', {'recettes': recettes})

@login_required
def ajouter_recette(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST)
        if form.is_valid():
            recette = form.save(commit=False)
            recette.auteur = request.user
            recette.save()
            return redirect('liste_recettes')
    else:
        form = RecetteForm()
    return render(request, 'recettes/formulaire.html', {'form': form, 'action': 'Ajouter'})

@login_required
def modifier_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk, auteur=request.user)
    if request.method == 'POST':
        form = RecetteForm(request.POST, instance=recette)
        if form.is_valid():
            form.save()
            return redirect('liste_recettes')
    else:
        form = RecetteForm(instance=recette)
    return render(request, 'recettes/formulaire.html', {'form': form, 'action': 'Modifier'})