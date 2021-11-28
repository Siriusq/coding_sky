from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages  
from django.core.paginator import Paginator  
from django.http import HttpResponseNotFound  
from faunadb import query as q  
import pytz  
from faunadb.objects import Ref  
from faunadb.client import FaunaClient  
import hashlib  
import datetime  

# Create your views here.

def index(request):
    context_dict = {}
    response = render(request, 'coding/index.html', context=context_dict)
    return response

def gamePage(request):
    #context_dict = {}
    response = render(request, 'coding/game.html')
    return response

def solutionPage(request):
    #context_dict = {}
    response = render(request, 'coding/solution.html')
    return response

def register(request):
   if request.method == "POST":
       username = request.POST.get("username").strip().lower()
       email = request.POST.get("email").strip().lower()
       password = request.POST.get("password")

       try:
           user = client.query(q.get(q.match(q.index("users_index"), username)))
           messages.add_message(request, messages.INFO, 'User already exists with that username.')
           return redirect("coding:register")
       except:
           user = client.query(q.create(q.collection("users"), {
               "data": {
                   "username": username,
                   "email": email,
                   "password": hashlib.sha512(password.encode()).hexdigest(),
                   "date": datetime.datetime.now(pytz.UTC)
               }
           }))
           messages.add_message(request, messages.INFO, 'Registration successful.')
           return redirect("coding:login")
   return render(request,"coding/register.html")

def login(request):
   if request.method == "POST":
       username = request.POST.get("username").strip().lower()
       password = request.POST.get("password")

       try:
           user = client.query(q.get(q.match(q.index("users_index"), username)))
           if hashlib.sha512(password.encode()).hexdigest() == user["data"]["password"]:
               request.session["user"] = {
                   "id": user["ref"].id(),
                   "username": user["data"]["username"]
               }
               return redirect("coding:dashboard")
           else:
               raise Exception()
       except:
           messages.add_message(request, messages.INFO,"You have supplied invalid login credentials, please try again!", "danger")
           return redirect("coding:login")
   return render(request,"coding/login.html")

def dashboard(request):
   if "user" in request.session:
       user=request.session["user"]["username"]
       context={"user":user}
       return render(request,"coding/dashboard.html",context)
   else:
       return HttpResponseNotFound("Page not found")

client = FaunaClient(secret="fnAEZFNGj0AAxmy5D2ICavNypkhZwCvmfLZXfkyx", domain="db.eu.fauna.com")  
indexes = client.query(q.paginate(q.indexes()))