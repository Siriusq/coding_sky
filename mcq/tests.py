from django.test import TestCase
from .models import *

class AnswerTestSuite(TestCase):
    def setUp(self):
        mcq = MCQQuestion.objects.create(answer_order = 'awo')
        self.aw = Answer.objects.create(content = "awt", question = mcq)
    
    def test_str(self):
        self.assertEqual(self.aw.__str__(), self.aw.content)

class MCQQuestionTestSuite(TestCase):
    def setUp(self):
        self.mcq = MCQQuestion.objects.create(answer_order = 'content')

    def test_check_if_correct(self):
        aw = Answer.objects.create(content = "awt", question = self.mcq, correct = True,)
        a = self.mcq.check_if_correct(aw.id)
        self.assertTrue(a)

    def test_check_if_incorrect(self):
        aw1 = Answer.objects.create(content = "awt1", question = self.mcq, correct = False,)
        b = self.mcq.check_if_correct(aw1.id)
        self.assertFalse(b)