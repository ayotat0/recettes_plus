from django.test import TestCase


from django.urls import reverse
from django.contrib.auth.models import User

class ComptesTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_inscription_view(self):
        response = self.client.get(reverse('inscription'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comptes/inscription.html')

    def test_connexion_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('connexion'))
        self.assertEqual(response.status_code, 200)

