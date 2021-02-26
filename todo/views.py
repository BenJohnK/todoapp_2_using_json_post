from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    tasks=Task.objects.all()
    return render(request,"todo/index.html",{'tasks':tasks})
