from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from django.urls import resolve
from lockdown.decorators import lockdown

@lockdown()
def index(request):
    return render(request, "main/index.html")

def correct(request):
    all_videos = Video.objects.all()
    context = {
        'videos': all_videos
    }
    return render(request, "main/realone.html", context)