from django.urls import path, include
from coding.views import *
from django.conf import settings  
from django.conf.urls.static import static  

app_name = 'coding'

urlpatterns = [
    path('', index,name='index'),
    path("login", login, name="login"),  
    path("dashboard", dashboard, name="dashboard"),  
    #path("quiz", quiz, name="quiz"),  
    path("register", register, name="register"),  
    #path("create-quiz", create_quiz, name="create-quiz"),  
    #path("create-questions", create_question, name="create-question"),  
    #path("answer-quiz/<slug>", answer_quiz, name="answer-quiz"), 
    path('game/', gamePage,name='gamePage'),
    path('solution/', solutionPage,name='solutionPage'),
]