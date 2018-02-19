from django.conf.urls import url
from dju_wsclient import views

urlpatterns = [
    url(r'^$',views.accueil,name='home'),
    url(r'^ws/([a-z0-9]+).json$', views.trucjson),
    url(r'^ws/load/([a-z0-9]+).json$', views.loadjson),
]
