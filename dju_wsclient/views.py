from django.http import HttpResponse
from django.shortcuts import render

from dju_wsclient.models import WSService, get_last, updatejson

# Create your views here.
def accueil(request):
    return render(request,'dju_wsclient/accueil.html')


def trucjson(request, truc):
    print('truc = ' + truc)
    service = WSService.objects.get(portail_name=truc)
    print('service ' + service.__str__())
    json = get_last(service)
    response = HttpResponse(json)
    response['Content-Type'] = 'application/json;charset=utf-8'
    return response

              
def loadjson(request, truc):
    print('truc = ' + truc)
    service = WSService.objects.get(portail_name=truc)
    print('service ' + service.__str__())
    updatejson(service)
    response = HttpResponse('DONE')
    return response
