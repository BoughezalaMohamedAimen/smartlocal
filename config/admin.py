from django.contrib import admin
from .models import *


class IdentifiantAdmin(admin.ModelAdmin):

    # some code...

    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Identifiant.objects.exists():
            retVal = False
        return retVal

class ConfigAdmin(admin.ModelAdmin):

    # some code...

    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Config.objects.exists():
            retVal = False
        return retVal





admin.site.register(Config,ConfigAdmin)


admin.site.register(Identifiant,IdentifiantAdmin)
