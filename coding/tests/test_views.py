from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.urls import resolve
from django.test import Client

from ..models import *
from ..views import *

class ViewTestCase(TestCase):
    def setUp(self):
        self.testUser = User.objects.create_superuser(
            username="utest", email="utest@a.com", password="123456"
        )

class indexTestCase(TestCase):
    def test_url_index(self):
        found = resolve("/")
        self.assertEqual(found.func, index)

    def test_index_Res(self):
        c = Client()
        response = c.post('/')
        self.assertIn(b"Homepage\n | Coding Sky", response.content)

class indexCodingTestCase(TestCase):
    def test_url_index(self):
        found = resolve("/coding/")
        self.assertEqual(found.func, index)

    def test_index_Res(self):
        c = Client()
        response = c.post('/coding/')
        self.assertIn(b"Homepage\n | Coding Sky", response.content)

class gamePageTestCase(TestCase):
    def test_url_gamePage(self):
        found = resolve("/coding/game/")
        self.assertEqual(found.func, gamePage)
    
    def test_gamePage_Res(self):
        c = Client()
        response = c.post('/coding/game/')
        self.assertIn(b" Game\n | Coding Sky", response.content)
    
class solutionPageTestCase(TestCase):
    def test_url_solutionPage(self):
        found = resolve("/coding/solution/")
        self.assertEqual(found.func, solutionPage)

    def test_login_Res(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        c.login(username='testuser', password='12345')
        response = c.post('/coding/solution/')
        self.assertTrue(response.content.startswith(b"<!--"))
        self.assertIn(b"SolutionPage\n | Coding Sky", response.content)
        self.assertTrue(response.content.endswith(b"</html>"))

    def test_not_login_Res(self):
        c = Client()
        response = c.post('/coding/solution/')
        self.assertNotIn(b"SolutionPage\n | Coding Sky", response.content)

class aboutTestCase(TestCase):
    def test_url_about(self):
        found = resolve("/coding/about/")
        self.assertEqual(found.func, about)

    def test_about_Res(self):
        c = Client()
        response = c.post('/coding/about/')
        self.assertIn(b" About\n | Coding Sky", response.content)

class errorTestCase(TestCase):
    def test_error_Res(self):
        c = Client()
        response = c.post('/coding/err/')
        self.assertNotEqual(response.status_code, 200)

class registerTestCase(TestCase):
    def test_url_reg(self):
        found = resolve("/coding/register/")
        self.assertEqual(found.func, register_user)

    def test_not_reg_Res(self):
        c = Client()
        response = c.post('/coding/register/')
        self.assertIn(b"Register", response.content)

    def test_reg_Res(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        c.login(username='testuser', password='12345')
        response = c.post('/coding/register/')
        self.assertNotIn(b"Register", response.content)

class loginTestCase(TestCase):
    def test_url_login(self):
        found = resolve("/coding/login/")
        self.assertEqual(found.func, login_user)

    def test_login_Res(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        c.login(username='testuser', password='12345')
        response = c.post('/coding/login/', username='testuser', password='12345')
        self.assertNotIn(b"Login", response.content)

class logoutTestCase(TestCase):
    def test_logout_Res(self):
        c = Client()
        response = c.post('/coding/logout/')
        self.assertEqual(response.status_code, 302)

class authTestCase(TestCase):
    def test_wrong_quiz_Res(self):
        c = Client()
        response = c.post('/coding/quizzes/')
        self.assertNotIn(b"Quiz", response.content)

    def test_wrong_record_Res(self):
        c = Client()
        response = c.post('/coding/progress/')
        self.assertNotIn(b"Record", response.content)