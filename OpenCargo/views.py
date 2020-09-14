
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def preguntas(request):
    return render(request, "preguntas.html")

def sign_upCLIENTE(request):
    return render(request, "sign_upCLIENTE.html")

def sign_upCONDUCTOR(request):
    return render(request, "sign_upCONDUCTOR.html")