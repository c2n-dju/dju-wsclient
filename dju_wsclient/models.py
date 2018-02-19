# -*- coding: utf-8 -*-

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
import json
import os
import random
import requests

class WSSite(models.Model):
    WSS='WSS'
    WOSS='WOSS'
    RHS='RHS'
    SITE_CHOICES = (
        (WSS, 'WS'),
        (WOSS, 'WOS'),
        (RHS, 'RH'),
    )
    site = models.CharField(max_length=15, choices=SITE_CHOICES, blank=False, unique=True)
    sitename = models.CharField(max_length=63, blank=False)

    def __str__(self):
        return self.site


class WSService(models.Model):
    site = models.ForeignKey(WSSite)
    service = models.CharField(max_length=63, blank=False)
    portail_name = models.CharField(max_length=63,
                                    blank=False,
                                    unique=True)
        
    def __str__(self):
        return self.site.__str__() + '/' + self.service
    
    class Meta:
        unique_together = ('site', 'service')

    
class WSCache(models.Model):
    service = models.ForeignKey(WSService)
    first_update = models.DateTimeField(blank=False, default=0)
    last_update = models.DateTimeField(blank=False, default=0)
    json = JSONField()

    def __str__(self):
        return self.service.__str__() + ' ' + str(self.last_update)


""" objects of same service are supposed to be chronologically indexed"""
def get_last(service):
    r = WSCache.objects.filter(service=service).last()
    return r.json if r != None else ''

""" check that objects of a given service are chronologically indexed"""
def check_caches_of_service(service):
    r = WSCache.objects.filter(service=service).order_by('id').values_list('last_update')
    r0 = r[0]
    for r in r[1:]:
        assert(r0[0] < r[0])
        r0 = r


""" check that objects of same service are chronologically indexed"""
def check_caches():
    for s in WSService.objects.all():
        check_caches_of_service(s)


def getjson(service):
    url = service.site.sitename + service.service
    a = requests.get(url, auth=(os.environ['LDAP_LOGIN'],
                                os.environ['LDAP_PASSWORD']))
    if not a.ok:
        a.raise_for_status()
    return a.json()

def updatejson(service):
    now = timezone.now()
    jnew = getjson(service)
    print('jnew = ' + str(jnew))
    if jnew == "":
        return
    r = WSCache.objects.filter(service=service).last()
    if r != None and r.json == jnew:
        r.last_update = now
    else:
        r = WSCache(service=service, first_update=now, last_update=now, json=jnew)
    r.save()

