from django.conf.urls import url
from dju_wsclient import views

urlpatterns = [
    url(r'^$',views.accueil,name='home'),
    url(r'^ws/personne.json$',views.personnejson),
    url(r'^ws/structure.json$',views.structurejson),
]
