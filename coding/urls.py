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
    path("login", login, name="login"),  
    path("logout", logout, name="logout"),  
    #path("register", register, name="register"),  
    path('game/', gamePage,name='gamePage'),
    path('solution/', solutionPage,name='solutionPage'),

    url(regex=r'^$', view=index, name='index'),
                        url(regex=r'^login/$', view=login_user, name='login'),
                        url(regex=r'^logout/$', view=logout_user, name='logout'),
                       url(regex=r'^quizzes/$',
                           view=QuizListView.as_view(),
                           name='quiz_index'),

                       url(regex=r'^category/$',
                           view=CategoriesListView.as_view(),
                           name='quiz_category_list_all'),

                       url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
                           view=ViewQuizListByCategory.as_view(),
                           name='quiz_category_list_matching'),

                       url(regex=r'^progress/$',
                           view=QuizUserProgressView.as_view(),
                           name='quiz_progress'),

                       url(regex=r'^marking/$',
                           view=QuizMarkingList.as_view(),
                           name='quiz_marking'),

                       url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                           view=QuizMarkingDetail.as_view(),
                           name='quiz_marking_detail'),

                       #  passes variable 'quiz_name' to quiz_take view
                       url(regex=r'^(?P<slug>[\w-]+)/$',
                           view=QuizDetailView.as_view(),
                           name='quiz_start_page'),

                       url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
                           view=QuizTake.as_view(),
                           name='quiz_question'),
]