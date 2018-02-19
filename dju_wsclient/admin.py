from django.contrib import admin
from dju_wsclient.models import WSSite, WSService, WSCache

admin.site.register(WSSite)
admin.site.register(WSService)
admin.site.register(WSCache)
