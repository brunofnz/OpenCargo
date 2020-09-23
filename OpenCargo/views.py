
from django.shortcuts import render

def landingPage(request):
    return render(request, "index.html")

def preguntas(request):
    return render(request, "preguntas.html")

