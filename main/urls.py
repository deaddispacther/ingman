from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("feet/", views.correct, name="feet"),
    path("massage/", views.correct, name="massage"),
    path("taz/", views.correct, name="taz"),
    path("tazbott/", views.correct, name="tazbott"),
    path("spine/", views.correct, name="spine"),
    path("posture/", views.correct, name="posture"),
    path("pill/", views.correct, name="pill"),
    path("fulltrain/", views.correct, name="fulltrain"),
    path("exercise/", views.correct, name="exercise"),
    path("butt/", views.correct, name="butt"),
    path("breath/", views.correct, name="breath"),
]