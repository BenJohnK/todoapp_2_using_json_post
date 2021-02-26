from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .models import *
# Create your views here.

def home(request):
    tasks=Task.objects.all()
    return render(request,"todo/index.html",{'tasks':tasks})

def titlesubmit(request):
    data=json.loads(request.body)
    title=data['title']
    print(title)
    # t=Task()
    # t.title=title
    # t.save()
    Task.objects.create(title=title)
    return JsonResponse("success",safe=False)