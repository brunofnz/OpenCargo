from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sign_upCLIENTE(request):
    return render(request, "sign_upCLIENTE.html")

def sign_upCONDUCTOR(request):
    return render(request, "sign_upCONDUCTOR.html")