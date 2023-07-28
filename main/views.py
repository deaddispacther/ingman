from django.shortcuts import render
from django.http import HttpResponse

def correct(request):
    return HttpResponse("")

def index(request):
    return render(request, "main/index.html")