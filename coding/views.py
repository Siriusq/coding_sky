from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {}
    response = render(request, 'coding/index.html', context=context_dict)
    return response

def gamePage(request):
    #context_dict = {}
    response = render(request, 'coding/game.html')
    return response