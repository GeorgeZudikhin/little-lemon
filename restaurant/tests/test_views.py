from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APITestCase

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ice Cream", price=80, inventory=100)
        Menu.objects.create(title="Cake", price=120, inventory=50)
        
    def test_get_all_menu_items(self):
        url = reverse('menu-items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
