from django.urls import path, include
from coding.views import *
from .views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake, index, login_user, logout_user
from django.urls import path
from django.conf.urls import url

app_name = 'coding'

urlpatterns = [
    path('', index,name='index'),
    path("login/", login_user, name="login"),  
    path("logout/", logout_user, name="logout"),  
    path("register/", register_user, name="register"),  
    path('game/', gamePage,name='gamePage'),
    path('solution/', solutionPage,name='solutionPage'),
    path('about/', about,name='about'),
    path('download/', downloadPage,name='downloadPage'),
    path('quizzes/', QuizListView.as_view(),name='quiz_index'),
    path('category/', CategoriesListView.as_view(),name='quiz_category_list_all'),
    path('progress/', QuizUserProgressView.as_view(),name='quiz_progress'),
    path('marking/', QuizMarkingList.as_view(),name='quiz_marking'),

    path('category/<slug:category_name>/', ViewQuizListByCategory.as_view(),name='quiz_category_list_matching'),
    path('marking/<slug:pk>/', QuizMarkingDetail.as_view(),name='quiz_marking_detail'),
    path('<slug:slug>/', QuizDetailView.as_view(),name='quiz_start_page'),#  passes variable 'quiz_name' to quiz_take view
    path('<slug:quiz_name>/take/', QuizTake.as_view(),name='quiz_question'),
]