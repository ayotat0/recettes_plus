# recettes/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recette
from django.urls import reverse

class RecetteTests(TestCase):
    def setUp(self):
        # Set up a user and a sample recipe to work with
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.recette = Recette.objects.create(
            titre='Test Recipe',
            description='Test desc',
            ingredients='Test ingr',
            etapes='Test steps',
            temps_preparation=30,
            difficulte='Facile',
            auteur=self.user
        )
        # Log in the user for tests needing authentication
        self.client.login(username='testuser', password='testpass123')

    def test_recette_str(self):
        # Check if the recipe title shows up correctly as a string
        self.assertEqual(str(self.recette), 'Test Recipe')

    def test_recette_list_view(self):
        # Make sure the recipe list page loads and uses the right template
        response = self.client.get('/recettes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recettes/liste.html')

    def test_adding_a_recipe(self):
        # Let’s try adding a new recipe and see if it works
        new_recipe_data = {
            'titre': 'New Recipe Test',
            'description': 'A new test recipe',
            'ingredients': 'Flour, Water',
            'etapes': 'Mix and bake',
            'temps_preparation': 40,
            'difficulte': 'Moyen',
            'categorie': ''  # Leaving category blank since it’s optional
        }
        response = self.client.post(reverse('ajouter_recette'), new_recipe_data)
        # Should redirect back to the list after adding
        self.assertEqual(response.status_code, 302)
        # Check if the recipe was actually saved
        self.assertEqual(Recette.objects.count(), 2)  # Original + new one

    def test_modifying_a_recipe(self):
        # Time to test if I can change an existing recipe
        updated_data = {
            'titre': 'Updated Recipe',
            'description': 'Updated desc',
            'ingredients': 'Updated ingr',
            'etapes': 'Updated steps',
            'temps_preparation': 50,
            'difficulte': 'Difficile',
            'categorie': ''
        }
        response = self.client.post(reverse('modifier_recette', kwargs={'pk': self.recette.pk}), updated_data)
        # Should redirect after a successful update
        self.assertEqual(response.status_code, 302)
        # Refresh the recipe from the database to check the change
        self.recette.refresh_from_db()
        self.assertEqual(self.recette.titre, 'Updated Recipe')

    def test_no_access_without_login(self):
        # Let’s see what happens if someone tries to see the list without logging in
        self.client.logout()  # Log out to test unauthorized access
        response = self.client.get('/recettes/')
        # Should redirect to login page
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/comptes/connexion/'))