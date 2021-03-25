from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Review, Worker
# Create your views here.

def index(request):
    return render(request, 'base.html')

def home(request):    
    return render(request, 'home.html')
    # return HttpResponse("<h1>Home</h1>")

def about(request):
    return render(request, 'about.html')

def figma(request):
    return render(request, 'figma.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')