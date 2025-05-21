from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Desserts')
        for i in range(15):
            Recipe.objects.create(title=f'Recipe {i}', category=self.category)

    def test_main_view_status_code(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_main_view_template_used(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'main.html')

    def test_main_view_context_max_10_recipes(self):
        response = self.client.get(reverse('main'))
        self.assertLessEqual(len(response.context['recipes']), 10)

    def test_category_detail_view_status_code(self):
        response = self.client.get(reverse('category_detail', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_template_used(self):
        response = self.client.get(reverse('category_detail', args=[self.category.id]))
        self.assertTemplateUsed(response, 'category_detail.html')

    def test_category_detail_view_context(self):
        response = self.client.get(reverse('category_detail', args=[self.category.id]))
        self.assertEqual(len(response.context['recipes']), 15)