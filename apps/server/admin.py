from django.contrib import admin
from apps.server.models import Server

class ServerAdmin(admin.ModelAdmin):
    list_display = ['name', 'logging']

admin.site.register(Server, ServerAdmin)
