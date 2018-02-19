from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def accueil(request):
    return render(request,'dju_wsclient/accueil.html')


def personnejson(request):
    return render(HTTPRESPONSE('Stay tuned!'))


def structurejson(request):
    return render(HTTPRESPONSE('Stay tuned!'))
              

