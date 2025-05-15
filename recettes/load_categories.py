from .models import Categorie

def load_categories():
    categories = ['Dessert', 'Entrée', 'Salé', 'Plat Principal', 'Végétarien']
    for nom in categories:
        Categorie.objects.get_or_create(nom=nom)

if __name__ == "__main__":
    load_categories()
    print("Catégories ajoutées avec succès !")