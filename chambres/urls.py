from django.contrib import admin
from django.urls import path,re_path
from .views import *
from .api import *

urlpatterns = [
        path('<int:id>', SingleChambre.as_view(),name='SingleChambre'),
        path('commande/<int:device>/<int:commande>',ChangeEtat.as_view(),name='ChangeEtat'),
        path('commande/<int:device>/',ChangeEtat.as_view(),name='ChangeEtat'),
        path('chalenge',NewChalenge.as_view(),name='NewChalenge'),



        #------------------API ROUTES-----------------------------------#
        path('api', ChambreListApi.as_view(),name='ChambreListApi'),
        path('commandes/api', CommandeListApi.as_view(),name='CommandeListApi'),


        path('sync',InternetSynch.as_view(),name='InternetSync'),
]
