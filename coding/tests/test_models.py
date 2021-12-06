from django.db.models.fields import files
from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User

from ..models import *

class CategoryTestCase(TestCase):
    def setUp(self):
        self.newCate = Category.objects.create(category = "Cat Test")
    
    def test_cate_name(self):
        self.assertEqual(self.newCate.__str__(), self.newCate.category)

class QuizTestCase(TestCase):
    def setUp(self):
        self.newQuiz = Quiz.objects.create(title = "QuizTest")
    
    def test_str(self):
        self.assertEqual(self.newQuiz.__str__(), self.newQuiz.title)

    def test_get_questions(self):
        question1 = Question.objects.create(content = "QuestionTest1")
        question2 = Question.objects.create(content = "QuestionTest2")
        question1.quiz.add(self.newQuiz)
        question2.quiz.add(self.newQuiz) 
        ques = (question1,question2)
        self.assertEqual(tuple(self.newQuiz.get_questions()), ques)

    def test_get_max_score(self):
        question1 = Question.objects.create(content = "QuestionTest1")
        question2 = Question.objects.create(content = "QuestionTest2")
        question1.quiz.add(self.newQuiz)
        question2.quiz.add(self.newQuiz) 
        self.assertEqual(self.newQuiz.get_max_score, 2)

    def test_anon_score_id(self):
        exp = str(self.newQuiz.id) + "_score"
        self.assertEqual(self.newQuiz.anon_score_id(), exp)

    def test_anon_q_list(self):
        exp = str(self.newQuiz.id) + "_q_list"
        self.assertEqual(self.newQuiz.anon_q_list(), exp)

    def test_anon_q_data(self):
        exp = str(self.newQuiz.id) + "_data"
        self.assertEqual(self.newQuiz.anon_q_data(), exp)

class ProgressTestCase(TestCase):
    def setUp(self):
        testUser = User.objects.create_superuser(
            username="utest", email="utest@a.com", password="123456"
        )
        self.newPg = Progress.objects.create(
            user = testUser,
        )

    def test_str(self):
        exp = 'utest - '
        self.assertEqual(self.newPg.__str__(),exp)

    def test_list_all_cat_scores_none(self):
        self.assertEqual(self.newPg.list_all_cat_scores, {})

    def test_list_all_cat_scores(self):
        newCat = Category.objects.create(category = "Cat Test")
        self.assertEqual(self.newPg.list_all_cat_scores, {'Cat Test': [0, 0]})

    def test_show_exams(self):
        testUser1 = User.objects.create_superuser(
            username="utest1", email="utest@a.com", password="123456"
        )
        self.newPg1 = Progress.objects.create(
            user = testUser1,
        )
        newQuiz = Quiz.objects.create(title = "QuizTest")
        newQuiz.exam_paper = True
        newSitting = Sitting.objects.create(
            user = testUser1, 
            quiz = newQuiz,
            current_score = 3,
            complete = True,
        )
        self.assertEqual(str(tuple(self.newPg1.show_exams())), '(<Sitting: Sitting object (1)>,)')

class SittingTestCaseSpecial(TestCase):   
    def test_get_first_question(self):
        newQuiz = Quiz.objects.create(title = "QuizTest")
        question1 = Question.objects.create(content = "QuestionTest1")
        question2 = Question.objects.create(content = "QuestionTest2")
        question1.quiz.add(newQuiz)
        question2.quiz.add(newQuiz) 
        testUser = User.objects.create_superuser(
            username="utest", email="utest@a.com", password="123456"
        )
        self.newSit = Sitting.objects.create(
            user = testUser,
            quiz = newQuiz,
            question_order = 1,
            question_list = "1,2",
            current_score = 1,
            complete = True,
        )
        self.assertEqual(self.newSit.get_first_question(), question1)
    
    def test_remove_first_question(self):
        newQuiz = Quiz.objects.create(title = "QuizTest")
        question1 = Question.objects.create(content = "QuestionTest1")
        question2 = Question.objects.create(content = "QuestionTest2")
        question1.quiz.add(newQuiz)
        question2.quiz.add(newQuiz) 
        testUser = User.objects.create_superuser(
            username="utest", email="utest@a.com", password="123456"
        )
        self.newSit = Sitting.objects.create(
            user = testUser,
            quiz = newQuiz,
            question_order = 1,
            question_list = "1,2",
            current_score = 1,
            complete = True,
        )
        self.newSit.remove_first_question()
        self.assertEqual(self.newSit.question_list, str(question2.id))

    def test_remove_incorrect_question(self):
        newQuiz = Quiz.objects.create(title = "QuizTest")
        question1 = Question.objects.create(content = "QuestionTest1")
        question2 = Question.objects.create(content = "QuestionTest2")
        question1.quiz.add(newQuiz)
        question2.quiz.add(newQuiz) 
        testUser = User.objects.create_superuser(
            username="utest", email="utest@a.com", password="123456"
        )
        self.newSit = Sitting.objects.create(
            user = testUser,
            quiz = newQuiz,
            question_order = 1,
            question_list = "1,2",
            current_score = 1,
            complete = True,
        )
        self.newSit.add_incorrect_question(question1)
        epc = []
        self.newSit.remove_incorrect_question(question1)
        self.newSit.get_incorrect_questions
        self.assertEqual(self.newSit.get_incorrect_questions, epc)  

    
class SittingTestCase(TestCase):   
    def setUp(self):
        newQuiz = Quiz.objects.create(title = "QuizTest")
        question1 = Question.objects.create(content = "QuestionTest1")
        question2 = Question.objects.create(content = "QuestionTest2")
        question1.quiz.add(newQuiz)
        question2.quiz.add(newQuiz) 
        testUser = User.objects.create_superuser(
            username="utest", email="utest@a.com", password="123456"
        )
        self.newSit = Sitting.objects.create(
            user = testUser,
            quiz = newQuiz,
            question_order = 1,
            question_list = "1,2",
            current_score = 1,
            complete = True,
        )

    def test_add_to_score(self):
        x = 3
        epc = self.newSit.current_score + x
        self.newSit.add_to_score(x)
        self.assertEqual(self.newSit.current_score, epc)

    def test_get_current_score(self):
        epc = self.newSit.current_score
        self.assertEqual(self.newSit.get_current_score, epc)

    def test_question_ids(self):
        epc = '<bound method Sitting._question_ids of <Sitting: Sitting object (1)>>'
        self.assertEqual(str(self.newSit._question_ids), epc)


class SittingTestCaseIncorrect(TestCase):   
    def setUp(self):
        newQuiz = Quiz.objects.create(title = "QuizTest")
        question1 = Question.objects.create(content = "QuestionTest1")
        question2 = Question.objects.create(content = "QuestionTest2")
        question1.quiz.add(newQuiz)
        question2.quiz.add(newQuiz) 
        testUser = User.objects.create_superuser(
            username="utest", email="utest@a.com", password="123456"
        )
        self.newSit = Sitting.objects.create(
            user = testUser,
            quiz = newQuiz,
            question_order = 1,
            question_list = "1,2",
            current_score = 1,
            complete = True,
        )
        self.newSit.add_incorrect_question(question1)

    def test_get_incorrect_questions(self):
        epc = [1]
        self.newSit.get_incorrect_questions
        self.assertEqual(self.newSit.get_incorrect_questions, epc)



class QuestionTestCase(TestCase):
    def setUp(self):
        self.newQuestion = Question.objects.create(content = "QuestionTest")

    def test_str(self):
        self.assertEqual(self.newQuestion.__str__(), self.newQuestion.content)
