from django.urls import path, include
from coding.views import *
from django.conf import settings  
from django.conf.urls.static import static  

app_name = 'coding'

urlpatterns = [
    path('', index,name='index'),
    path("login", login, name="login"),  
    path("logout", logout, name="logout"),  
    path("dashboard", dashboard, name="dashboard"),  
    path("quiz", quiz, name="quiz"),  
    path("register", register, name="register"),  
    path("create_quiz", create_quiz, name="create_quiz"),  
    path("create_questions", create_question, name="create_question"),  
    path("answer_quiz/<slug>", answer_quiz, name="answer_quiz"), 
    path('game/', gamePage,name='gamePage'),
    path('solution/', solutionPage,name='solutionPage'),
]