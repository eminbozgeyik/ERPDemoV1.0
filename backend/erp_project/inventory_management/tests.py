from django.test import TestCase
from rest_framework.test import APIClient
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

class CategoryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='Test Category')

    def test_category_detail_view(self):
        response = self.client.get(f'/categories/{self.category.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Category')

    def test_category_list_view(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

class ItemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='Test Category')
        self.item = Item.objects.create(name='Test Item', category=self.category, quantity=1)

    def test_item_detail_view(self):
        response = self.client.get(f'/items/{self.item.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Item')

    def test_item_list_view(self):
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)