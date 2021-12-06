from django.test import TestCase

# Create your tests here.
class TestTestCase(TestCase):
    def test_test(self):
        self.assertEqual(1 + 1, 2)