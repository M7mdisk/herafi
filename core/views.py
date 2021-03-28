from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Review, Worker, Profession
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
import json
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, 'base.html')

def home(request):    
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def figma(request):
    return render(request, 'figma.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def search(request):
    workers_list = Worker.objects.all()
    professions_list = Profession.objects.all()
    serialized_workers = serializers.serialize('geojson', workers_list)
    context = {
        "location":"Kuwait, Salmiya",
        "workers":workers_list,
        "workers_json":serialized_workers,
        "professions":professions_list
    }
    print(serialized_workers)
    return render(request, 'search.html',context)