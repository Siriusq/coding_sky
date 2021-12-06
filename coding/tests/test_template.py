import os
from django.test import TestCase
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

class TemplateTests(TestCase):
    def test_index_temp_use(self):
        url = reverse('coding:index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'coding/base.html')
        self.assertTemplateUsed(response, 'coding/index.html')
    
    def test_about_temp_use(self):
        url = reverse('coding:about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'coding/base.html')
        self.assertTemplateUsed(response, 'coding/about.html')

    def test_game_temp_use(self):
        url = reverse('coding:gamePage')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'coding/base.html')
        self.assertTemplateUsed(response, 'coding/game.html')
    
    def test_solution_temp_use(self):
        url = reverse('coding:solutionPage')
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        c.login(username='testuser', password='12345')
        response = c.post(url)
        self.assertTemplateUsed(response, 'coding/base.html')
        self.assertTemplateUsed(response, 'coding/solution.html')

    def test_quiz_temp_use(self):
        url = reverse('coding:quiz_index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'coding/base.html')
        self.assertTemplateUsed(response, 'coding/quiz_list.html')

    def test_cat_temp_use(self):
        url = reverse('coding:quiz_category_list_all')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'coding/base.html')
        self.assertTemplateUsed(response, 'coding/category_list.html')