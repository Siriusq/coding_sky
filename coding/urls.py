from django.urls import path
from django.urls.resolvers import URLPattern
from coding.views import *
from django.contrib import admin

app_name = 'coding'

urlpatterns = [
    path('', index,name='index'),
    path('register/', registerPage,name='register'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('addQuestion/', addQuestion,name='addQuestion'),
    path('game/', gamePage,name='gamePage'),
]