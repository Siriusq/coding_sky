import os
import importlib
from django.test import TestCase
from django.conf import settings

class AppTestSuite(TestCase):
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.coding_app_dir = os.path.join(self.project_base_dir, 'coding')

    def test_coding_app(self):
        coding_app = 'coding' in settings.INSTALLED_APPS
        self.assertTrue(coding_app)

    def test_mcq_app(self):
        mcq_app = 'mcq' in settings.INSTALLED_APPS
        self.assertTrue(mcq_app)

    def test_crispy_forms_app(self):
        crispy_forms_app = 'crispy_forms' in settings.INSTALLED_APPS
        self.assertTrue(crispy_forms_app)

class DeployTestSuite(TestCase):
    #Test for Deployment
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.coding_app_dir = os.path.join(self.project_base_dir, 'coding')

    def test_debug(self):
        debugClose = settings.DEBUG
        self.assertFalse(debugClose)

    def test_allowed_hosts(self):
        allowedHosts = settings.ALLOWED_HOSTS
        epc = ['*', 'testserver']
        self.assertEqual(allowedHosts, epc)