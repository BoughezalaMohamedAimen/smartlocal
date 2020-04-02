from django.contrib import admin
from .models import *



class ChambreAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')


admin.site.register(Chambre,ChambreAdmin)



class CommandeAdmin(admin.ModelAdmin):
    list_filter=['chambre','type']
    list_display = ('id','type','chambre', 'nom')

class ChalengeAdmin(admin.ModelAdmin):
    list_display = ('heure','ip','chalenge', 'result')


admin.site.register(Commande,CommandeAdmin)

admin.site.register(Chalenge,ChalengeAdmin)
#
#
# class PriseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nom')
#
#
# admin.site.register(Prise,PriseAdmin)
#
#
# class RideauAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nom')
#
#
# admin.site.register(Rideau,RideauAdmin)
